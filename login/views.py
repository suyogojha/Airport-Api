from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.
def dohome(request):
    c = {}
    c.update(csrf(request))
    return render(request,'home.html')
def dologin(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html')
def doauth(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)
    print(user)
    print("hi")
    if user is not None:
        auth.login(request, user)
        print("valid")
        return render(request,'dashboard.html')
    else:
        print("invalid")
        return  render(request,'login.html',{'message':'Invalid Credential'})
@login_required(login_url='/login/login')
def dologout(request):
    auth.logout(request)
    return render(request,'home.html')