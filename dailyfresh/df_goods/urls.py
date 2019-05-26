from django.urls import path,include,re_path
from  df_goods import  views
urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    re_path(r'^(\d+)/$',views.detail),
]