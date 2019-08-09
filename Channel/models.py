from django.db import models
from django.utils.safestring import mark_safe
from Category.models import City, Category
from Category.consts import STATUS_ON, STATUS_OFF
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    id = models.AutoField(verbose_name="Id", primary_key=True, null=False, db_index=True)
    title = models.CharField(verbose_name="标题", max_length=256, null=False, db_index=True)
    sub_title = models.CharField(verbose_name="副标题", max_length=512, null=True, default="")
    poster = models.URLField(verbose_name="新闻头图", null=True, default="")
    weight = models.FloatField(verbose_name="权重", null=True, default=0)
    city_set = models.ManyToManyField(City, verbose_name="可见城市", related_name="city_news_tag")
    category_set = models.ManyToManyField(Category, verbose_name="分类", related_name="category_news_tag")
    content = RichTextUploadingField(verbose_name="内容", null=False)
    status = models.SmallIntegerField(verbose_name="媒体状态", null=True, db_index=True, default=0,
                                      choices=((STATUS_OFF, "下线"), (STATUS_ON, "上线")))
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __unicode__(self):
        return self.title

    def city_tag(self):
        return ",".join([city.city_name for city in list(self.city_set.all())])

    city_tag.allow_tags = True
    city_tag.short_description = u"可见城市"

    def category_tag(self):
        return ",".join([category.category_name for category in list(self.category_set.all())])

    category_tag.allow_tags = True
    category_tag.short_description = u"所属分类"

    @mark_safe
    def poster_tag(self):
        if self.poster == "":
            return ""
        else:
            return '<img src="%s" width="230px" height="150px"/>' % self.poster

    poster_tag.allow_tags = True
    poster_tag.short_description = u"头图"

    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = u"新闻"
        permissions = [(city.city_code, city.city_name) for city in City.objects.all()]
        permissions += [(category.category_code, category.category_name) for category in Category.objects.all()]


class Activity(News):
    class Meta:
        proxy = True
        verbose_name = u"活动"
        verbose_name_plural = u"活动"
