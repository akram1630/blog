from django.urls import path 
from . import views
urlpatterns = [
    path('y/',views.y),
    path('z',views.z), # we shouldn't put '/' at final
    ######################################################
    path('',views.home,name='home'),
    path('books/',views.books),
    path('customer/',views.customer),



]
