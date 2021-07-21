#from django.http import HttpResponse as hp
from django.shortcuts import render
from .models import fuckoff as fk

# Create your views here.
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