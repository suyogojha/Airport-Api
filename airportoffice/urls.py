from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$',views.doinit,name='doinit'),
    url(r'^flboarding',views.doflboarding,name='doflboarding'),
    url(r'^flupdate',views.doflupdate,name='doflupdate'),
    url(r'^boarding',views.doboarding,name='doboarding'),
    url(r'^flightupdate',views.doflightupdate,name='doflightupdate'),
    url(r'^reset',views.doreset,name='doreset'),
]