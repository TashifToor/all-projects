from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

 

#JOEgoldberg123!

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        redirect('/Login')
    return render(request,'index.html')
def Loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'Login.html')
            
    # A backend authenticated the credential
    
    # No backend authenticated the credentials

        
    return render(request,'Login.html')
def Logoutuser(request):
    logout(request)
    return render(request,'Login.html')
