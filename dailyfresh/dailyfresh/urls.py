"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path
from df_user import  urls
from df_goods import  urls
from df_cart import urls
from df_order import urls
from haystack import urls
urlpatterns = [
    path('',include('df_goods.urls')),
    path('user/',include('df_user.urls')),
    path('cart/',include('df_cart.urls')),
    re_path(r'^tinymce/',include('tinymce.urls')),
    re_path(r'order/',include('df_order.urls')),
    re_path(r'^search/',include('haystack.urls')),
    path('admin/',admin.site.urls),
]
