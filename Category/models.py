from django.db import models


class Category(models.Model):
    category_id = models.AutoField(verbose_name="类别Id", primary_key=True, unique=True, null=False)
    category_code = models.CharField(verbose_name="类别代码", max_length=32, null=False, unique=True)
    category_name = models.CharField(verbose_name="类别名称", max_length=256, default="", null=False)
    weight = models.FloatField(verbose_name="权重", null=True, default=0)

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class City(models.Model):
    city_id = models.AutoField(verbose_name="城市Id", primary_key=True, unique=True, null=False)
    city_code = models.CharField(verbose_name="城市代码", max_length=32, null=False, unique=True)
    city_name = models.CharField(verbose_name="城市名称", max_length=256, default="", null=False)
    weight = models.FloatField(verbose_name="权重", null=True, default=0)

    def __unicode__(self):
        return self.city_name

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = u"城市"
