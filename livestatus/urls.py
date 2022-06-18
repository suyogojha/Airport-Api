from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.doinit,name='doinit'),
    url(r'^lpassogood',views.dolpassogood,name='dolpassogood'),
    url(r'^lflight',views.dolflight,name='dolfight'),
    url(r'^livef',views.dolivef,name='dolivef'),
    url(r'^livepg',views.dolivepg,name='dolivepg'),
]