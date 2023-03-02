
from django.urls import path
from django.http import HttpRequest, HttpResponse, JsonResponse
def index(request:HttpRequest):
    a = request.GET['a']
    
    print(a)
    return JsonResponse({'a':a})

urlpatterns = [
    path('', index),
]
