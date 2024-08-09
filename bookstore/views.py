from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm,CreateNewUser,CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login  , logout 
# Create your views here.
####################################################################################  
def y(request):
    return HttpResponse('yyyyyyyyyyyyyyyy')
################################################################################################
def z(request):
    return HttpResponse('zzzzzzzzzzzzzzzzz')
################################################################################################
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
################################################################################################
def books(request): 
    books = Book.objects.all() # objects of class 
    return render(request=request , template_name='bookstore/books.html',context={'books': books })
################################################################################################
# def customer(request,pk):
#     customer = Customer.objects.get(id=pk)  
#     orders = customer.order_set.all()
#     total_orders = orders.count()

#     #searchFilter = OrderFilter(request.GET , queryset=orders)
#     #orders = searchFilter.qs
#     myContext = {
#         'customer': customer ,
#         #'myFilter': searchFilter ,
#         'orders': orders,
#         'total_orders': total_orders
#     }
#     return render(request=request , template_name='bookstore/customer.html',context=myContext)
################################################################################################
# def create(request): 
#     form = OrderForm()
#     if request.method == 'POST':
#        print(request.POST) # :<QueryDict: {'csrfmiddlewaretoken': ['t1tXOUX9aBJUdJ6ezJJUWdMWBC5L1qTIQrHzP0mycZ8WTeivSWIEURfweAEUdqje'], 'customer': ['2'], 'book': ['2'], 'tags': ['2'], 'status': ['in progress']}>
#        form = OrderForm(request.POST) #the new object
#        if form.is_valid():
#            form.save()
#            return redirect('/')
#            #return redirect('/books')
#     context = {'form':form}
#     return render(request=request , template_name='bookstore/my_order_form.html', context=context )
####################################################################################  
#with filtering :
def customer(request,pk):
    customer = Customer.objects.get(id=pk)  
    orders = customer.order_set.all()
    total_orders = orders.count()
    searchFilter = OrderFilter(request.GET , queryset=orders)
    orders = searchFilter.qs #override all order to qs : queryset
    myContext = {
        'customer': customer ,
        'orders': orders,
        'total_orders': total_orders,   
        'myFilter' : searchFilter
    }
    return render(request=request , template_name='bookstore/customer.html',context=myContext)
################################################################################################
#create many orders of specific user in one time :
def create(request,pk): #pk of customer 
    orderFormSet = inlineformset_factory(Customer,Order,fields=('book', 'status'),extra=8)
    customer = Customer.objects.get(id=pk)
    #queryset=Order.objects.none() to not show any existed order 
    formSet = orderFormSet(queryset=Order.objects.none() , instance=customer)
    if request.method == 'POST':
       print(request.POST) # :<QueryDict: {'csrfmiddlewaretoken': ['t1tXOUX9aBJUdJ6ezJJUWdMWBC5L1qTIQrHzP0mycZ8WTeivSWIEURfweAEUdqje'], 'customer': ['2'], 'book': ['2'], 'tags': ['2'], 'status': ['in progress']}>
       formSet = orderFormSet(request.POST , instance=customer)
       if formSet.is_valid():
           formSet.save()
           return redirect('/')
           #return redirect('/books')
    context = {'formSet':formSet}
    return render(request=request , template_name='bookstore/my_order_form.html', context=context )
################################################################################################
def update(request,pk): 
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) #to fill the form with ancient order
    if request.method == 'POST': 
       form = OrderForm(request.POST, instance=order) #to update the ancient order with new per user
       if form.is_valid():
           form.save()
           return redirect('/')
    context = {'form':form}
    return render(request , 'bookstore/my_order_form.html', context )
################################################################################################
def delete(request , pk):
    order = Order.objects.get(id=pk)  
    if request.method == "POST": #we used post http cuz it's protected by csrf-token
        order.delete() 
        return redirect('/')
    myContext = {"order" : order}    
    return render( request=request , template_name= 'bookstore/delete_form.html',context=myContext)    
################################################################################################
# def login(request):  
#     if request.user.is_authenticated:
#         return redirect('home')
#     else: 
#         context = {}
#     return render(request=request,template_name='bookstore/login.html',context=context )
################################################################################################
# def register(request):   
#     #form = UserCreationForm(request.POST) #aint from forms.py
#     form = CreateNewUser(request.POST) # i modified UserCreationForm to CreateNewUser in forms.py 
#     if request.method == 'POST': 
#         if form.is_valid():
#             form.save()#store it in DataBase
#             return redirect('/')
#         else:
#             print('not valid') 
#     context = {'form':form}
#     return render(request=request ,template_name= 'bookstore/register.html',context= context )
################################################################################################                           
def register(request):   
    #form = UserCreationForm(request.POST) #aint from forms.py
    form = CreateNewUser(request.POST) # i modified UserCreationForm to CreateNewUser in forms.py 
    if request.method == 'POST': 
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            #messages will be sent as a variable in href next page
            messages.success(request , username + ' Created Successfully !')
            return redirect('login')  
    #     form = CreateNewUser(request.POST)
    #         recaptcha_response = request.POST.get('g-recaptcha-response')
    #         data = {
    #            'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
    #            'response' : recaptcha_response
    #         }
    #         r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
    #         result = r.json()
    #         if result['success']:
    #             
               
    #             return redirect('login')  
    #         else:
    #             messages.error(request ,  ' invalid Recaptcha please try again!')  
    context = {'form':form}
    return render(request=request ,template_name= 'bookstore/register.html',context= context )
################################################################################################                           
#we can't name this def login()
def userLogin(request):  
    if request.method == 'POST': 
        username = request.POST.get('username')  
        password = request.POST.get('password')
        print(username,'+++',password)
        user = authenticate(request , username=username, password=password)
        if user is not None: #None = not exist
            login(request, user) 
            return redirect('home')
        else:
            messages.info(request, 'Credentials error')
    
    context = {}

    return render(request , 'bookstore/login.html', context )        
################################################################################################                                                      
def userLogout(request):  
    logout(request) #function i imported
    return redirect('login') 

