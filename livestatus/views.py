from django.shortcuts import render
from datetime import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from schedule.models import Schedule,Flight
from livestatus.models import Status,Passenger,Goods,LiveFlight
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/login')
def doinit(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'livestatus.html')
@login_required(login_url='/login/login')
def dolivef(request):
    return render(request,'LiveFlight.html')
@login_required(login_url='/login/login')
def dolivepg(request):
    return render(request,'LiveGoods.html')
@login_required(login_url='/login/login')
def dolpassogood(request):
    c={}
    c.update(csrf(request))
    pnr=request.POST.get('pnr','')
    pasogood=Status.objects.filter(pnr=pnr)
    if len(pasogood)==0:
        c['m']="No Such PNR Exist"
    else:
        c['q']=pasogood[0]
        c['m']="Status :"
        print(pasogood)
    return render(request,'LiveGoods.html',c)
@login_required(login_url='/login/login')
def dolflight(request):
    c = {}
    c.update(csrf(request))
    flightid=request.POST.get('flightid','')
    flgt=LiveFlight.objects.filter(flightid=flightid)
    if len(flgt)==0:
        c['m']="No Such Flight Exist"
    else:
        c['q'] = flgt[0]
        c['m'] = "Status :"
    return render(request,'LiveFlight.html',c)