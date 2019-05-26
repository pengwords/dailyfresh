from django.contrib import redirects
from django.urls import path, re_path, include
from . import  views
urlpatterns = [
    re_path(r'^$',views.cart),
    re_path(r'^add_(\d+)_(\d+)/$',views.add),
    re_path(r'^edit(\d+)_(\d+)/$',views.edit),
    re_path(r'^delete_(\d+)/$',views.delete),
    re_path(r'^order/$',views.order),
]