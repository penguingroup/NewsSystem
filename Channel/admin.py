from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from Category.consts import STATUS_ON, STATUS_OFF
from Channel.models import News, Activity
from Channel.utils import get_permission, put_to_es


class CityFilter(SimpleListFilter):
    title = "可见城市"
    parameter_name = "city_filter"

    def lookups(self, request, model_admin):
        cities, _ = get_permission(request)
        return ((city.city_id, city.city_name) for city in cities)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(city_set__city_id=self.value()).distinct()


class CategoryFilter(SimpleListFilter):
    title = "分类"
    parameter_name = "category_filter"

    def lookups(self, request, model_admin):
        _, categories = get_permission(request)
        return ((category.category_id, category.category_name) for category in categories)

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(category_set__category_id=self.value()).distinct()


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'weight', 'city_tag', 'category_tag', 'status', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = (
        ('title', 'sub_title',),
        ('status',),
        ('weight',),
        ('poster', 'poster_tag',),
        ('city_tag',),
        ('category_tag',),
        ('city_set', 'category_set',),
        ('content',),
    )
    list_editable = ('weight',)
    readonly_fields = ('city_tag', 'category_tag', 'status', 'poster_tag')
    list_filter = (CityFilter, CategoryFilter, 'status')
    list_per_page = 50
    ordering = ('-weight', '-updated_at', '-created_at',)
    filter_horizontal = ('city_set', 'category_set')
    actions = ['publish_selected', 'rollback_selected']

    def get_queryset(self, request):
        query_set = super(NewsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return query_set
        cities, categories = get_permission(request)
        return query_set.filter(city_set__in=cities, category_set__in=categories).distinct()

    def publish_selected(self, request, queryset):
        news = News.objects.filter(id__in=[_.id for _ in queryset])
        news.update(status=STATUS_ON)
        for new in news:
            put_to_es(new.id, new.to_dict())
        self.message_user(request, u"选中的%d条新闻上线成功" % queryset.count())

    publish_selected.short_description = u"上线选中的新闻"

    def rollback_selected(self, request, queryset):
        news = News.objects.filter(id__in=[_.id for _ in queryset])
        news.update(status=STATUS_OFF)
        for new in news:
            put_to_es(new.id, new.to_dict())
        self.message_user(request, u"选中的%d个新闻下线成功" % queryset.count())

    rollback_selected.short_description = u"下线选中的新闻"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['object_id'] = int(object_id)
        return super(NewsAdmin, self).change_view(request,
                                                  object_id,
                                                  extra_context=extra_context)


class ActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Activity, ActivityAdmin)
