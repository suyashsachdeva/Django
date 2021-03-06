"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mkl.views import home_view, info_view, contact_view
from fuckoff.views import product_detail_view, product_create_view 

urlpatterns = [
    path('', home_view, name='HOME'),
    path('admin/', admin.site.urls),
    path('contact/',contact_view, name="CONTACT"),
    path('info/',info_view, name="INFO"),
    path('product/', product_detail_view),
    path('create/', product_create_view)
]
