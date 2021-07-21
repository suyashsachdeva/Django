from django.http import HttpResponse as hp
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return hp('<h1>HOME</h1>')
    return render(request, 'home.html', {})

def info_view(request, *args, **kwargs):
    #return hp('<h1>INFO</h1>')
    return render(request, 'info.html', {})

def contact_view(request,*args, **kwargs):
    return render(request, 'contact.html', {})