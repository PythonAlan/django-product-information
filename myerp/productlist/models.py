from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
import os




class Product(models.Model):
    category = models.CharField(u'目录',max_length=20)
    sku = models.CharField(max_length=20)
    name = models.CharField(u'产品名称',max_length=200)
    description = models.TextField(u'产品描述')
    image = models.URLField(u'产品图片',null=True,blank=True)
    owner = models.CharField(u'开发者',max_length=20, default="A组")
    price = models.FloatField(u'采购价',)
    weight = models.IntegerField(u'重量g')
    volume = models.FloatField(u'体积m³',default=0.001)
    cn_us_cost = models.FloatField(u'美国本地小包$',default=1)
    us_second_cost = models.FloatField(u'美国海外小包$',default=1)
    cn_uk_cost = models.FloatField(u'英国本地小包£',default=1)
    uk_second_cost = models.FloatField(u'英国海外小包£',default=1)
    cn_de_cost = models.FloatField(u'德国本地小包€',default=1)
    de_second_cost = models.FloatField(u'德国海外小包€',default=1)
    cn_au_cost = models.FloatField(u'澳洲本地小包$',default=1)
    au_second_cost = models.FloatField(u'澳洲海外小包$',default=1)

    class Meta:
        ordering = ('price',)
        verbose_name = '产品列表'
        verbose_name_plural = '产品列表'

    def __str__(self):
        return self.name


