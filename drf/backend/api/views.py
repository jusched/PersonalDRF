from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    data = {"message": "First API", "status": 200}
    return JsonResponse(data)
