from django.db import models
from Category.consts import *


class Category(models.Model):
    category_id = models.AutoField(verbose_name="类别Id", primary_key=True, unique=True, null=False)
    category_code = models.CharField(verbose_name="类别代码", max_length=32, null=False, unique=True)
    category_name = models.CharField(verbose_name="类别名称", max_length=256, default="", null=False)
    weight = models.FloatField(verbose_name="权重", null=True, default=0)
    status = models.SmallIntegerField(verbose_name="媒体状态", null=True, db_index=True, default=0,
                                      choices=((STATUS_OFF, "下线"), (STATUS_ON, "上线")))

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name

    def to_dict(self):
        return {
            "id": self.category_id,
            "code": self.category_code,
            "name": self.category_name,
        }

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class City(models.Model):
    city_id = models.AutoField(verbose_name="城市Id", primary_key=True, unique=True, null=False)
    city_code = models.CharField(verbose_name="城市代码", max_length=32, null=False, unique=True)
    city_name = models.CharField(verbose_name="城市名称", max_length=256, default="", null=False)
    weight = models.FloatField(verbose_name="权重", null=True, default=0)
    status = models.SmallIntegerField(verbose_name="媒体状态", null=True, db_index=True, default=0,
                                      choices=((STATUS_OFF, "下线"), (STATUS_ON, "上线")))

    def __unicode__(self):
        return self.city_name

    def __str__(self):
        return self.city_name

    def to_dict(self):
        return {
            "id": self.city_id,
            "code": self.city_code,
            "name": self.city_name,
        }

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = u"城市"
