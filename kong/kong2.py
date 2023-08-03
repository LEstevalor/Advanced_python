# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging
import time
from typing import List

from bk_plugin_framework.kit import Plugin
from pathos.multiprocessing import ProcessingPool as _Pool
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import product, groupby
from operator import attrgetter

# 自定义事件上报处理器DEMO
from prometheus_client.exposition import default_handler, push_to_gateway, generate_latest
from prometheus_client.registry import CollectorRegistry
from pytz import timezone

from apps.clb_v2.models import BizConfigModel, BizCLBListModel
from apps.clb_v2.utils.constants import CLB_NAMESPACE
from bk_plugin.handlers.base import register_handler, BaseHandler
from bk_plugin.handlers.metric import Gauge
from apps.clb_v2.gateways.cloud import get_region_list, get_clb_list, get_clb_monitor_info, get_metric_list
from apps.clb_v2.utils.tools import list_of_groups, get_hourly_chime
from tencentcloud.clb.v20180317.models import LoadBalancer

logger = logging.getLogger("bk_plugin")

# 接口单次最大查询CLB实例数量
MAX_CLB_LIST_LEN = 10
# 查询CLB接口限频
MAX_CLB_API_FREQ = 5
# 查询MONITOR接口限频
MAX_MONITOR_API_FREQ = 20
# 查询5min时间范围数据
TIME_CAP = 5
# 进程池大小
POOL_SIZE = 20


@register_handler("clb_v2")
class CLBV2Handler(BaseHandler):
    """
    采集当前插件运行环境的
    """
    name = "clb_v2"
    REGISTRY = None

    def __init__(self, token, target_url, **kwargs):
        super().__init__(token, target_url, **kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

            biz = BizConfigModel.objects.get(bk_biz_id=self.bk_biz_id)
            self.secret_id = biz.secret_id
            self.secret_key = biz.secret_key

        if not self.metric_list:
            raise Plugin.Error("监控指标列表不可为空")

    def push(self):
        def bk_handler(url, method, timeout, headers, data):
            # 定义基于监控 token 的上报 handler 方法
            def handle():
                headers.append(("X-BK-TOKEN", self.token))
                default_handler(url, method, timeout, headers, data)()

            return handle

        def create_load_balancer_from_clb(clb_info):
            # 根据clb的负载均衡id、vip与VPC ID创建LoadBalancer对象
            load_balancer = LoadBalancer()
            load_balancer.LoadBalancerId = clb_info.LoadBalancerId
            load_balancer.LoadBalancerVips = [clb_info.LoadBalancerVips, ]
            load_balancer.VpcId = clb_info.VpcId
            return load_balancer

        def process_metric_info(region, metric_name, clb_list: List[LoadBalancer]):
            # 根据业务对应地域region、指标名称metric、对应地域下分组的clb列表做指标查询
            # 获取一系列业务地域分组后的CLB的指标信息
            monitor_info = get_clb_monitor_info(region, metric_name, start_time, end_time, clb_list,
                                                self.is_internal_api, self.handler_name, self.secret_id,
                                                self.secret_key)
            if not monitor_info:
                logger.warning("can not get data,region:{},clb:{},metric:{}".format(region, clb_list, metric_name))
                return

            for item in monitor_info:
                # item:({clb},({timestamp},{value}))
                registry = CollectorRegistry(auto_describe=True)
                # 根据metric动态声明指标变量并赋值
                metric = registry._names_to_collectors.get(metric_name)
                if metric is None:
                    metric = Gauge(metric_name, metric_map.get(metric_name),
                                   labelnames=["bk_biz_id", "region", "vip"], registry=registry)
                metric.labels(bk_biz_id=self.bk_biz_id, region=region, vip=item[0]).set_time(item[1][0]).set(
                    item[1][1])
                # 携带instance维度，上报到蓝鲸监控自定义指标(全业务维度)
                push_to_gateway(gateway=self.target_url,
                                job=self.name,
                                registry=registry,
                                grouping_key={"instance": item[0]},
                                handler=bk_handler)
                logger.info("handler({}) push data with: \n"
                            "{}".format(self.name, generate_latest(registry).decode("utf8")))

        def process_region(region, clb_list=None):
            if not clb_list:
                # 根据region得到业务在对应地域下的CLB实例list
                clb_list = get_clb_list(region, self.is_internal_api, self.handler_name, self.secret_id, self.secret_key)
                if not clb_list:
                    return

            # 判断是否存储映射结构，无则存储
            if not BizCLBListModel.objects.filter(bk_biz_id=self.bk_biz_id, handler_name=self.handler_name,
                                                  is_internal_api=self.is_internal_api).exists():
                model_clb_list = [BizCLBListModel(bk_biz_id=self.bk_biz_id, handler_name=self.handler_name,
                                                  is_internal_api=self.is_internal_api, region=region, VpcId=clb.VpcId,
                                                  LoadBalancerId=clb.LoadBalancerId,
                                                  LoadBalancerVips=clb.LoadBalancerVips[0]
                                                  ) for clb in clb_list if clb.LoadBalancerVips]
                BizCLBListModel.objects.bulk_create(model_clb_list)

            # 将CLB列表切分成10个一组
            clb_list_group = list_of_groups(self.clb_list, MAX_CLB_LIST_LEN)

            # 创建 ThreadPoolExecutor 线程池
            with ThreadPoolExecutor(max_workers=MAX_MONITOR_API_FREQ) as executor:
                tasks = []
                # 组合metric和CLB实例，做笛卡尔积，查询对应的监控指标数据
                for metric_name, clb_list in product(self.metric_list, clb_list_group):
                    f = executor.submit(process_metric_info, region, metric_name, clb_list)
                    tasks.append(f)
                # 等待 ThreadPoolExecutor 线程池中的所有任务完成
                for f in tasks:
                    f.result()

        # 预设查询起始时间
        dt_now = datetime.now(tz=timezone("Asia/Shanghai"))
        start_time = get_hourly_chime(dt_now, -TIME_CAP, "min")
        end_time = get_hourly_chime(dt_now, 0, "min")
        # 获取指标映射Map
        metric_info = get_metric_list("ap-shanghai", CLB_NAMESPACE.get(self.handler_name), self.is_internal_api, self.secret_id, self.secret_key)
        metric_map = {metric.MetricName: metric.MetricCName for metric in metric_info.MetricSet}

        # 查看数据库是否存入多级映射关系
        select_clb_list = BizCLBListModel.objects.filter(bk_biz_id=self.bk_biz_id, handler_name=self.handler_name,
                                                         is_internal_api=self.is_internal_api).exclude(LoadBalancerId=None)
        is_get_clb_model = select_clb_list.exists()

        region_list = []
        clb_list_group = []
        if is_get_clb_model:
            # 按region对clb实例分组
            for region, clbs in groupby(select_clb_list, key=attrgetter('region')):
                clb_list = [create_load_balancer_from_clb(clb) for clb in clbs]
                region_list.append(region)
                clb_list_group.append(clb_list)
        else:
            # 获取CLB地域list
            region_list = get_region_list(self.is_internal_api, self.secret_id, self.secret_key)

        region_list_group = list_of_groups(region_list, MAX_CLB_API_FREQ)
        for region_list in region_list_group:
            with _Pool(processes=POOL_SIZE) as pool:
                # 处理所有的region，将任务分配给进程池中的进程并发处理
                if is_get_clb_model:
                    pool.map(process_region, region_list, clb_list_group)
                else:
                    pool.map(process_region, region_list)
            time.sleep(1)
