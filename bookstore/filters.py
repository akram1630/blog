import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet): 
    class Meta: #meta called also inner class
        model = Order   
        fields = '__all__' #default  fields of the form
        #fields = ['book' , 'status']   
        #exclude = ['book' , 'status'] #delete them from form      