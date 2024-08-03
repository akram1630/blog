from django.urls import path 
from . import views
urlpatterns = [
    path('y/',views.y),
    path('z/',views.z),
    ######################################################
    path('',views.home),



]
