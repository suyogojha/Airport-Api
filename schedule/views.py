from time import time
from datetime import datetime

from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.
from schedule.models import Schedule, Flight
from livestatus.models import LiveFlight
@login_required(login_url='/login/login')
def dosch(request):
    c = {}
    c.update(csrf(request))
    return render(request,'chooseschedule.html')
@login_required(login_url='/login/login')
def donew(request):
    return render(request,'createschedule.html')
@login_required(login_url='/login/login')
def docreateschedule(request):
    flightid=request.POST.get('flightid','')
    count=request.POST.get('count','')
    sunday =False
    monday=False
    tuesday=False
    wednesday=False
    thursday = False
    friday = False
    saturday = False
    if (request.POST.get('sunday','') == "sunday"):
        sunday = True
    if (request.POST.get('monday', '') =='monday'):
        monday = True
    if (request.POST.get('tuesday', '') == 'tuesday'):
        tuesday = True
    if (request.POST.get('wednesday', '') == 'wednesday'):
        wednesday = True
    if (request.POST.get('thursday', '') == 'thursday'):
        thursday = True
    if (request.POST.get('friday', '') == 'friday'):
        friday = True
    if (request.POST.get('saturday', '') == 'saturday'):
        saturday = True
    source=request.POST.get('source','')
    destination=request.POST.get('destination','')
    departures=datetime.strptime(request.POST.get('departures',''),'%H:%M')
    arrivald=datetime.strptime(request.POST.get('arrivald',''),'%H:%M')
    station=list()
    arrival=list()
    departure=list()
    station.append(source)
    departure.append(departures)
    for i in range(int(count)):
        station.append(request.POST.get('s'+str(i+1),''))
        arrival.append(datetime.strptime(request.POST.get('a'+str(i+1),''),'%H:%M'))
        departure.append(datetime.strptime(request.POST.get('d'+str(i+1),''),'%H:%M'))
    station.append(destination)
    arrival.append(arrivald)
    s=Flight(flightid=flightid,source=source,destination=destination,Monday=monday,Tuesday=tuesday,Wednesday=wednesday,Thursday=thursday,Friday=friday,Saturday=saturday,Sunday=sunday,passengercap=100)
    s.save()
    lv=LiveFlight(flightid=s,status="At Source")
    lv.save()
    n=len(station)
    for i in range(n-1):
        p=Schedule(flightid=s,source=station[i],destination=station[i+1],arrival=arrival[i],departure=departure[i])
        p.save();
    return render(request,'chooseschedule.html')
@login_required(login_url='/login/login')
def doupdate(request):
    return render(request,'updatecategory.html')
@login_required(login_url='/login/login')
def dodelete(request):
    return  render(request,'removeflight.html')
@login_required(login_url='/login/login')
def dochange(request):
    return render(request,'rescheduleflight.html')
@login_required(login_url='/login/login')
def doreschedule(request):
    return render(request,'rescheduleflight.html')
@login_required(login_url='/login/login')
def dochoosecategory(request):
    return render(request,'searchcategory.html')
@login_required(login_url='/login/login')
def dosearchid(request):
    return render(request,"flightid.html")
@login_required(login_url='/login/login')
def dosearchcity(request):
        return render(request,'srcdest.html')
@login_required(login_url='/login/login')
def docity(request):
    c={}
    c.update(csrf(request))
    source=request.POST.get('source','')
    destination=request.POST.get('destination','')
    cityquery=list()
    qs2=Schedule.objects.filter(destination=destination)
    for x in qs2:
        y=Schedule.objects.filter(source=source,flightid=x.flightid)
        if len(y)>0:
            cityquery.append(y[0])
            cityquery[-1].departure=x.departure
            cityquery[-1].arrival=y[0].arrival
            cityquery[-1].flightid=x.flightid
            cityquery[-1].source=source
            cityquery[-1].destination=destination
    if len(cityquery)==0:
        messages="No Such Flight Exist"
        return render(request,"srcdest.html",{"messages":messages})
    else:
        c['q']=cityquery
        for x in cityquery:
            print(x.flightid)
        return render(request,"srcdest.html",c)
@login_required(login_url='/login/login')
def doid(request):
    c={}
    c.update(csrf(request))

    fid=request.POST.get('flightid','')
    idquery=Schedule.objects.filter(flightid=fid).order_by('id')
    if len(idquery)==0:
        messages="No Such Flight Exist"
        return render(request,"flightid.html",{"messages":messages})
    else:
        c['q']=idquery
        for x in idquery:
            print(x.flightid)
        return render(request,'flightid.html',c)
@login_required(login_url='/login/login')
def doremove(request):
    flightid=request.POST.get('flightid','')
    removed=Flight.objects.filter(flightid=flightid)
    if len(removed)==0:
        messages="No Such Flight Exist"
        return render(request,"removeflight.html",{"messages":messages})
    else:
        Flight.objects.filter(flightid=flightid).delete()
        messages = "Deleted"
        return render(request, "removeflight.html", {'messages': messages})
@login_required(login_url='/login/login')
def doreschedule(request):
    flightid = request.POST.get('flightid', '')
    removed = Flight.objects.filter(flightid=flightid)
    if len(removed)==0:
        messages="No Such Flight Exist"
        return render(request,"removeflight.html",{"messages":messages})
    else:
        Flight.objects.filter(flightid=flightid).delete()
        count = request.POST.get('count', '')
        sunday = False
        monday = False
        tuesday = False
        wednesday = False
        thursday = False
        friday = False
        saturday = False
        if (request.POST.get('sunday', '') == "sunday"):
            sunday = True
        if (request.POST.get('monday', '') == 'monday'):
            monday = True
        if (request.POST.get('tuesday', '') == 'tuesday'):
            tuesday = True
        if (request.POST.get('wednesday', '') == 'wednesday'):
            wednesday = True
        if (request.POST.get('thursday', '') == 'thursday'):
            thursday = True
        if (request.POST.get('friday', '') == 'friday'):
            friday = True
        if (request.POST.get('saturday', '') == 'saturday'):
            saturday = True
        source = request.POST.get('source', '')
        destination = request.POST.get('destination', '')
        departures = datetime.strptime(request.POST.get('departures', ''),'%H:%M')
        arrivald = datetime.strptime(request.POST.get('arrivald', ''),'%H:%M')
        station = list()
        arrival = list()
        departure = list()
        station.append(source)
        departure.append(departures)
        for i in range(int(count)):
            station.append(request.POST.get('s' + str(i + 1), ''))
            arrival.append(datetime.strptime(request.POST.get('a' + str(i + 1), ''),'%H:%M'))
            departure.append(datetime.strptime(request.POST.get('d' + str(i + 1), ''),'%H:%M'))
        station.append(destination)
        arrival.append(arrivald)
        s = Flight(flightid=flightid, source=source, destination=destination, Monday=monday, Tuesday=tuesday,
               Wednesday=wednesday, Thursday=thursday, Friday=friday, Saturday=saturday, Sunday=sunday,
               passengercap=100)
        s.save()
        lv = LiveFlight(flightid=s, status="At Source")
        lv.save()
        n = len(station)
        for i in range(n - 1):
            p = Schedule(flightid=s, source=station[i], destination=station[i + 1], arrival=arrival[i],
                     departure=departure[i])
            p.save();
        messages = "Updated"
        return render(request, "rescheduleflight.html", {'messages': messages})