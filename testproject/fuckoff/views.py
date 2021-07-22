#from django.http import HttpResponse as hp
from django.shortcuts import render
from .models import fuckoff as fk
from .formm import ProductForm as pro, RawProform

# Create your views here.


def product_create_view(request):
    myform = RawProform(request.GET)
    if request.method == "POST":
        myform = RawProform(request.POST)
        if myform.is_valid():
            print(myform.cleaned_data)
            fk.objects.create(**myform.cleaned_data)
        else:
            print(myform.errors)
    content = {
        "form": myform
    }
    return render(request, "product/product_created.html", content)




# Core HTML
"""def product_create_view(request):
    # print(request.GET)
    # print(request.POST)
    title = request.POST.get('title')
    print(title)
    content = {}
    return render(request, "product/product_created.html", content)"""

# The easist way possible
"""def product_create_view(request):
    form = pro(request.POST or None)
    if form.is_valid():
        form.save()
        form = pro()
    # content = {
    #     "title" : obj.title,
    #     "description":obj.description
    # }

    content = {
        'form': form
    }
    return render(request, "product/product_create.html", content)"""


def product_detail_view(request):
    obj = fk.objects.get(id=2)
    # content = {
    #     "title" : obj.title,
    #     "description":obj.description
    # }

    content = {
        'object': obj
    }
    return render(request, "product/detail.html", content)