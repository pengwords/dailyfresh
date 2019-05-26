from django.urls import path, include, re_path
from df_user import views
urlpatterns = [
    re_path(r'^register/$', views.register),
    re_path(r'^register_handle/$', views.register_handel),
    re_path(r'^register_exist/$', views.register_exist),
    re_path(r'^login/$', views.login),
    re_path(r'^login_handel/$', views.login_handel),
    re_path(r'^logout$', views.logout),
    re_path(r'^info/$', views.info),
    re_path(r'^order/$', views.order),
    re_path(r'^site/$', views.site),
]
