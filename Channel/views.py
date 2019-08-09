from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.core.cache import cache


@staff_member_required
@require_http_methods(["POST"])
def push_to_es(request):
    result = {}
    try:
        object_id = request.POST["object_id"]
        status = request.POST["status"]
        result = {"status": status, "object_id": object_id}
        cache.set("test", result, timeout=600)
    except Exception as e:
        result["msg"] = e
    finally:
        return JsonResponse(result)
