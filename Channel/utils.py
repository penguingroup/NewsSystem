import json
import requests
from django.conf import settings
from Category.models import Category, City


def get_permission(request):
    """ 获取登录用户的权限列表

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
    """ 设置redis的prefix key

    :param key: redis的key
    :param key_prefix: key的前缀
    :param version: 版本号
    :return: 自定义的redis的key

    """
    return key


def put_to_es(index, put_data):
    """ 推送到ES

    :param index: ES的索引
    :param put_data: 需要存储的数据
    :return: ES的返回结果，字典结构

    """
    url = settings.ES_HOST % index
    response = requests.put(url, json=put_data, headers={"Content-Type": "application/json"})
    return json.loads(response.content)
