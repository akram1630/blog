from django.urls import path 
from . import views
urlpatterns = [
    path('y/',views.y),
    path('z',views.z), # we shouldn't put '/' at final
    ######################################################
    path('',views.home,name='home'),#name= it takes u to this url when click
    path('books/',views.books,name="books"),
    #path('customer/',views.customer,name='customer'), 
    #int or str for primaryKey (id)
    path('customer/<int:pk>/',views.customer,name='customer'),
    path('create/<int:pk>/',views.create,name='create'),
    path('update/<str:pk>/' ,views.update, name="update"),
    path('delete/<str:pk>/' ,views.delete, name="delete"),
    path('register/' ,views.register, name="register"),
    path('login/',views.login, name="login"),



]
