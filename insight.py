import time
import json
import requests

# TOKEN = os.environ.get("TOKEN", "")
COOKIE = "x_host_key_access=41e1a43afc6bc6ee33aae990f5d3a3cb12a59d20_s; x-client-ssid=1864d9cc290-a459db0e65d412fe2488224716860b91af6a8a7d; TCOA_TICKET=TOF4TeyJ2IjoiNCIsInRpZCI6InZ6end0VzNsb09NSDdEY25uRUZJNEJlUDhvc1Y0YzF2IiwiaXNzIjoiMTAuOTkuMjA4LjYxIiwiaWF0IjoiMjAyMy0wMy0wOFQxMDoyNTo1NC42MzY0NTI1MjMrMDg6MDAiLCJhdWQiOiIxMC44Ny4zOC4zNyIsImhhc2giOiI0RkI2RTY5NDA2OUU4OUZDMzkwMUUzMjlBOTE2MTFBRkY4RUI3NTM2QTkzMzE5NEE5OThGM0UzNTU2Rjc1NkYwIiwibmgiOiI4QUU5OTUzQ0VGQjlGNzU1OTYyNTJDMjAxMjZDODUyQkZCQ0VCNDc0NjFBQThCODZBNjhCRUExOENGOTgxMTFEIn0; TCOA=vzzwtW3loOMH7DcnnEFI4BeP8osV4c1v; RIO_TCOA_TICKET=tof:TOF4TeyJ2IjoiNCIsInRpZCI6InZ6end0VzNsb09NSDdEY25uRUZJNEJlUDhvc1Y0YzF2IiwiaXNzIjoiMTAuOTkuMjA4LjYxIiwiaWF0IjoiMjAyMy0wMy0wOFQxMDoyNTo1NC42MzY0NTI1MjMrMDg6MDAiLCJhdWQiOiIxMC44Ny4zOC4zNyIsImhhc2giOiI0RkI2RTY5NDA2OUU4OUZDMzkwMUUzMjlBOTE2MTFBRkY4RUI3NTM2QTkzMzE5NEE5OThGM0UzNTU2Rjc1NkYwIiwibmgiOiI4QUU5OTUzQ0VGQjlGNzU1OTYyNTJDMjAxMjZDODUyQkZCQ0VCNDc0NjFBQThCODZBNjhCRUExOENGOTgxMTFEIn0"

TGW_METRIC_LIST = {
    "sum_outtraffic": "出带宽",
    "sum_intraffic": "入带宽",
}

BUZ_TYPE = [20]  # TGW业务类型
LOGTYPE_ID = [5]  # 其他日志类型
LEVEL_ID = [5]  # 其他层级
CUSTOM_CONFIG = {  # 时间间隔聚合target数据
    "interval": "1m"
}


def get_tgw_monitor_info(term, target):
    url = "http://insight.woa.com/insight_go/api/v3/buz_logic/req"

    # 时间区间查询范围
    end_time = int(time.time())  # 时间戳取整（秒级）
    start_time = end_time - 24 * 60 * 60  # 获取前一天的数据
    range_filter = {"Gnow": {"start": start_time, "end": end_time}}
    # 按业务名称筛选
    terms_filter = {"AppName": term}

    try:
        params = {
            "buz_types": BUZ_TYPE,
            "level_id": LEVEL_ID,
            "logtype_id": LOGTYPE_ID,
            "targets": [target],
            "custom_config": CUSTOM_CONFIG,
            "terms_filter": terms_filter,
            "range_filter": range_filter
        }

        # headers = {'token': TOKEN, 'content-type': 'application/json;charset=utf8'}
        headers = {'cookie': COOKIE, 'content-type': 'application/json;charset=utf8'}
        ret = requests.post(url, json=params, headers=headers, timeout=10)

        # monitor_info = {}
        if ret.status_code == 200:
            monitor_info = json.loads(ret.text)
        else:
            raise Exception

        return monitor_info

    except Exception as err:
        print(err)


def get_tgw_map():
    url = "http://xxx/cgi-bin/fun_logic/bin/public_api/get_tgw_app_info.cgi"
    params = {
        "operator": "bkm_reporter",
        "busi_1st_id": [381353]
    }
    headers = {'content-type': 'application/json;charset=utf8'}
    try:
        tgw_all_data = requests.post(url, json=params, headers=headers)
        if tgw_all_data.status_code == 200:
            data = json.loads(tgw_all_data.text)
        else:
            raise Exception

        return data
    except Exception as err:
        print(err)
