#this file is to manage permission between users .
#like the middleware
from django.http import HttpResponse
from django.shortcuts import redirect

def notLoggedUsers(view_func):
    def wrapper_func(request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request , *args,**kwargs)
    return wrapper_func   

def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):
            group = None
            if request.user.groups.exists(): #if this user belongs to a group
                group = request.user.groups.all()[0].name #first group in list of groups django admin
            if group in allowedGroups:
                return view_func(request , *args , **kwargs)
            else:
                return redirect('user/')
        return wrapper_func
    return decorator   

def forAdmins(view_func):
    def wrapper_func(request , *args , **kwargs):
        group = None
        if request.user.groups.exists(): #if this user belongs to a group
            group = request.user.groups.all()[0].name #first group in list of groups django admin
        if group =='admin':
            return view_func(request , *args , **kwargs)
        if group =='customer':
            return redirect('user/')
        if group == None : #user doesn't belong to any group
            return HttpResponse('no exist group')
    return wrapper_func 
