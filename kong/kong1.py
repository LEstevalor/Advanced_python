# -*- coding: utf-8 -*-
from bkcrypto.contrib.django.fields import SymmetricTextField
from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    类型补充字段
    """
    create_on = models.DateTimeField("创建时间", auto_now_add=True)
    update_on = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        abstract = True


class BizConfigModel(BaseModel):
    product_id = models.IntegerField("产品ID", null=True, blank=True)
    product_name = models.CharField("产品名称", max_length=100, null=True, blank=True)
    biz_id = models.IntegerField("业务ID", unique=True)
    biz_name = models.CharField("业务名称", max_length=100)
    secret_id = SymmetricTextField("id", max_length=256, default="")
    secret_key = SymmetricTextField("key", max_length=256, default="")

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    @property
    def bk_product_tag(self):
        return "_".join([self.bk_product_name, str(self.bk_product_id)])

    class Meta:
        verbose_name = "业务信息"
        verbose_name_plural = verbose_name


class BizCLBListModel(BaseModel):
    biz_id = models.IntegerField("业务ID")
    region = models.CharField("地域", max_length=100)
    handler_name = models.CharField("handler类型", max_length=100)
    is_internal_api = models.BooleanField("是否用内网API", null=True, blank=True)
    VpcId = models.CharField("虚拟私有云ID", max_length=256)
    LoadBalancerId = models.CharField("负载均衡实例ID", max_length=256)
    LoadBalancerVips = models.CharField("负载均衡实例VIP", max_length=256)

    class Meta:
        verbose_name = "CLB实例信息"
        verbose_name_plural = verbose_name
