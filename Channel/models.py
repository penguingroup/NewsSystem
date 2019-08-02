from django.db import models
from Category.models import City, Category
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    id = models.AutoField(verbose_name="Id", primary_key=True, null=False, db_index=True)
    title = models.CharField(verbose_name="标题", max_length=256, null=False, db_index=True)
    sub_title = models.CharField(verbose_name="副标题", max_length=512, null=True, default="")
    city_set = models.ManyToManyField(City, verbose_name="可见城市", related_name="city_news_tag")
    category_set = models.ManyToManyField(Category, verbose_name="分类", related_name="category_news_tag")
    content = RichTextUploadingField(verbose_name="内容", null=False)
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
