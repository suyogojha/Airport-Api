from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.dohome,name='dohome'),
    url(r'^login',views.dologin,name='dologin'),
    url(r'^doauth',views.doauth,name='doauth'),
    url(r'^logout',views.dologout,name='dologout'),
]