from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

  
from .models import Order , Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order  
        fields ="__all__"
        #fields = ['book' , 'status']
        exclude = ['book' , 'status']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ="__all__"
        exclude = ['user'  ]

#to override the features of UserCreationForm :
class CreateNewUser(UserCreationForm):  
    class Meta:
        model = User
        fields =['username','email','password1','password2']

         