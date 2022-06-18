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
    return render(request, 'airportoffice.html')
@login_required(login_url='/login/login')
def doflboarding(request):
    return render(request,'boarding.html')
@login_required(login_url='/login/login')
def doflupdate(request):
    return render(request,'flightupdate.html')
@login_required(login_url='/login/login')
def doboarding(request):
    pnr=request.POST.get('pnr','')
    boardstatus=str("On Board")
    description=request.POST.get('flightid','')
    station=request.POST.get('station','')
    pasp=Passenger.objects.filter(pnr=pnr)
    pasg=Goods.objects.filter(pnr=pnr)
    messages=str()
    if len(pasp)>0:
        if pasp[0].flightid==description and pasp[0].source==station:
            brd=Status.objects.filter(pnr=pnr).update(boardstatus=boardstatus,description=description)
            messages="boarding Done"
        else:
            messages = "Flight PNR Mismatch"
    elif len(pasg) > 0:
        if pasg[0].flightid == description and pasg[0].source==station:
            brd = Status.objects.filter(pnr=pnr).update(boardstatus=boardstatus, description=description)
            messages='Boarding Done'
        else:
            messages = "Flight PNR Mismatch"
    else:
        messages="Flight PNR Mismatch"
    return render(request,"boarding.html",{'messages':messages})
@login_required(login_url='/login/login')
def doflightupdate(request):
    flightid=request.POST.get('flightid','')
    station=request.POST.get('station','')
    ardep=request.POST.get('ardep','')
    messages=str()
    if ardep=="arrived":
        stat=Status.objects.filter(description=flightid)
        if len(stat)==0:
            messages="No such Flight"
        else:
            for i in range(0,len(stat)):
                pas=Passenger.objects.filter(pnr=stat[i].pnr)
                if len(pas)>0:
                    if pas[0].destination==station:
                        Status.objects.filter(pnr=stat[i].pnr).update(boardstatus='At Destination',description=station)
                pas=Goods.objects.filter(pnr=stat[i].pnr)
                if len(pas)>0:
                    if pas[0].destination==station:
                        Status.objects.filter(pnr=stat[i].pnr).update(boardstatus='At Destination',description=station)
            flgt=LiveFlight.objects.filter(flightid=flightid).update(status="Arrived at "+station)
            messages = "Flight & Passenger Done"
    else:
        stat=LiveFlight.objects.filter(flightid=flightid)
        if len(stat)==0:
            messages="No such Flight"
        else:
            if station==Flight.objects.filter(flightid=flightid)[0].destination:
                flgt = LiveFlight.objects.filter(flightid=flightid).update(status="Reached Destination " + station)
            else:
                flgt=LiveFlight.objects.filter(flightid=flightid).update(status="Departed from "+station)
            messages="Flight & Passenger Done"
    return render(request,"flightupdate.html",{'messages':messages})
@login_required(login_url='/login/login')
def doreset(request):
    LiveFlight.objects.all().update(status='At Source')
    Status.objects.all().update(boardstatus="At Source",description=" ")
    return render(request,'dashboard.html')