from django.http import JsonResponse
from django.conf import urls
from django.views import debug


def handler404(request, *args, handler=urls.handler404, **kwargs):
    if request.content_type == 'application/json':
        return JsonResponse({'message': 'Not Found'}, status=404)
    return handler(request, *args, **kwargs)  # default 404

def handler500(request, *args, handler=urls.handler500, **kwargs):
    if request.content_type == 'application/json':
        return JsonResponse({'message': 'Server Error'}, status=500)
    return handler(request, *args, **kwargs)

def tech_404(*args, handler=debug.technical_404_response, **kwargs):
    return handler404(*args, handler=handler, **kwargs)

debug.technical_404_response = tech_404
