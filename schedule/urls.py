from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.dosch,name='dosch'),
    url(r'^new',views.donew,name='donew'),
    url(r'^createschedule',views.docreateschedule,name='docreateschedule'),
    url(r'^update',views.doupdate,name='doupdate'),
    url(r'^delete',views.dodelete,name='dodelete'),
    url(r'^change',views.dochange,name='dochange'),
    url(r'^remove',views.doremove,name='doremove'),
    url(r'^reschedule',views.doreschedule,name='doreschedule'),
    url(r'^choosecategory',views.dochoosecategory,name='dochoosecategory'),
    url(r'^searchid',views.dosearchid,name='dosearchid'),
    url(r'^searchcity',views.dosearchcity,name='dosearchcity'),
    url(r'^city',views.docity,name='docity'),
    url(r'^id',views.doid,name='doid'),
]