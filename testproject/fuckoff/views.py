#from django.http import HttpResponse as hp
from django.shortcuts import render
from .models import fuckoff as fk
from .formm import ProductForm as pro

# Create your views here.
def product_create_view(request):
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
    return render(request, "product/product_created.html", content)


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