from Category.models import Category, City


def get_permission(request):
    """

    :param request: Django 的request对象
    :return: 城市列表 分类列表

    """
    categories = Category.objects.all()
    cities = City.objects.all()
    city_list = [city for city in cities if request.user.has_perm("Channel.%s" % city.city_code)]
    category_list = [category for category in categories if
                     request.user.has_perm("Channel.%s" % category.category_code)]
    return city_list, category_list


def get_redis_prefix_key(key, key_prefix, version):
    """

    :param key: redis的key
    :param key_prefix: key的前缀
    :param version: 版本号
    :return: 自定义的redis的key

    """
    return key
