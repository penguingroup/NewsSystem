from django.contrib import admin
from Category.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_name")
    search_fields = ("category_name",)


class CityAdmin(admin.ModelAdmin):
    list_display = ("city_id", "city_name")
    search_fields = ("city_name",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.site_header = "企鹅社区运营后台"
admin.site.site_title = "企鹅社区运营管理系统"
