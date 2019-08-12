from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from Channel.models import News
from Channel.utils import *


@staff_member_required
@require_http_methods(["POST"])
def push_to_es(request):
    result = {}
    try:
        object_id = request.POST["object_id"]
        status = request.POST["status"]
        news = News.objects.get(id=object_id)
        news.status = status
        news.save()
        result = put_to_es(news.id, news.to_dict())
        if result["_shards"]["failed"] == 0:
            result["msg"] = "成功"
            result["code"] = 0
    except Exception as e:
        result["msg"] = e
    finally:
        return JsonResponse(result)
