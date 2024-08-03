from django.contrib import admin
from django.urls import path ,include
from django.http import HttpResponse

def x(request):
    return HttpResponse('heeeeeeeeeeeeeeeeeey')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('x/',x),
    path('',include('bookstore.urls')),

]
