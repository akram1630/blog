from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm,CreateNewUser,CustomerForm
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
    total_orders = orders.count()

    #searchFilter = OrderFilter(request.GET , queryset=orders)
    #orders = searchFilter.qs
    myContext = {
        'customer': customer ,
        #'myFilter': searchFilter ,
        'orders': orders,
        'total_orders': total_orders
    }
    return render(request=request , template_name='bookstore/customer.html',context=myContext)

def create(request): 
    form = OrderForm()
    if request.method == 'POST':
       print(request.POST) # :<QueryDict: {'csrfmiddlewaretoken': ['t1tXOUX9aBJUdJ6ezJJUWdMWBC5L1qTIQrHzP0mycZ8WTeivSWIEURfweAEUdqje'], 'customer': ['2'], 'book': ['2'], 'tags': ['2'], 'status': ['in progress']}>
       form = OrderForm(request.POST) #the new object
       if form.is_valid():
           form.save()
           return redirect('/')
           #return redirect('/books')
    context = {'form':form}

    return render(request , 'bookstore/my_order_form.html', context )