from django.contrib import admin
from django.core.cache import cache
from Category.models import *
from Category.consts import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_name", "weight", "status",)
    list_filter = ("status",)
    readonly_fields = ("status",)
    search_fields = ("category_name",)
    actions = ("publish_selected", "rollback_selected",)
    list_editable = ("weight",)
    ordering = ("-weight",)

    def publish_selected(self, request, queryset):
        Category.objects.filter(category_id__in=[_.category_id for _ in queryset]).update(status=STATUS_ON)
        categories = [category.to_dict() for category in Category.objects.filter(status=STATUS_ON).order_by("-weight")]
        cache.set(CATEGORY_REDIS_KEY, categories, REDIS_DEFAULT_TIME)
        self.message_user(request, u"选中的%d个分类启用成功" % queryset.count())

    publish_selected.short_description = u"启用选中的分类"

    def rollback_selected(self, request, queryset):
        Category.objects.filter(category_id__in=[_.category_id for _ in queryset]).update(status=STATUS_OFF)
        categories = [category.to_dict() for category in Category.objects.filter(status=STATUS_ON).order_by("-weight")]
        cache.set(CATEGORY_REDIS_KEY, categories, REDIS_DEFAULT_TIME)
        self.message_user(request, u"选中的%d个分类撤销成功" % queryset.count())

    rollback_selected.short_description = u"撤销选中的分类"


class CityAdmin(admin.ModelAdmin):
    list_display = ("city_id", "city_name", "weight", "status",)
    list_filter = ("status",)
    readonly_fields = ("status",)
    search_fields = ("city_name",)
    actions = ("publish_selected", "rollback_selected",)
    list_editable = ("weight",)
    ordering = ("-weight",)

    def publish_selected(self, request, queryset):
        City.objects.filter(city_id__in=[_.city_id for _ in queryset]).update(status=STATUS_ON)
        cities = [city.to_dict() for city in City.objects.filter(status=STATUS_ON).order_by("-weight")]
        cache.set(CITY_REDIS_KEY, cities, REDIS_DEFAULT_TIME)
        self.message_user(request, u"选中的%d个城市启用成功" % queryset.count())

    publish_selected.short_description = u"启用选中的城市"

    def rollback_selected(self, request, queryset):
        City.objects.filter(city_id__in=[_.city_id for _ in queryset]).update(status=STATUS_OFF)
        cities = [city.to_dict() for city in City.objects.filter(status=STATUS_ON).order_by("-weight")]
        cache.set(CITY_REDIS_KEY, cities, REDIS_DEFAULT_TIME)
        self.message_user(request, u"选中的%d个城市撤销成功" % queryset.count())

    rollback_selected.short_description = u"撤销选中的城市"


admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.site_header = "企鹅社区运营后台"
admin.site.site_title = "企鹅社区运营管理系统"
