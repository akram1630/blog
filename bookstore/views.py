from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def y(request):
    return HttpResponse('yyyyyyyyyyyyyyyy')
################################################################################################""

def z(request):
    return HttpResponse('zzzzzzzzzzzzzzzzz')
################################################################################################""
def home(request):   
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    total_p_orders = orders.filter(status='Pending').count()
    total_d_orders = orders.filter(status='Delivered').count()
    total_in_orders = orders.filter(status='in progress').count()
    total_out_orders = orders.filter(status='out of order').count()    
    myContext = {
               'customers': customers ,
               'orders': orders,  
               'total_orders': total_orders,
               'total_p_orders': total_p_orders,
               'total_d_orders': total_d_orders,
               'total_in_orders': total_in_orders,
               'total_out_orders': total_out_orders
               }
    return render(request=request , template_name='bookstore/dashboard.html',context=myContext)
################################################################################################""
def books(request): 
    books = Book.objects.all() # objects of class 
    return render(request=request , template_name='bookstore/books.html',context={'books': books })
################################################################################################""

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    #number_orders = orders.count()

    #searchFilter = OrderFilter(request.GET , queryset=orders)
    #orders = searchFilter.qs
    myContext = {
        'customer': customer ,
        #'myFilter': searchFilter ,
        'orders': orders,
        #'number_orders': number_orders
    }
    return render(request=request , template_name='bookstore/customer.html',context=myContext)