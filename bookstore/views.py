from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def y(request):
    return HttpResponse('yyyyyyyyyyyyyyyy')
def z(request):
    return HttpResponse('zzzzzzzzzzzzzzzzz')

def home(request):
    return render(request=request , template_name='bookstore/dashboard.html')