from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login



# password=Tashif$$$0
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/Login')
    return render(request,'index.html')
def LoginUser(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            
                
                
    # A backend authenticated the credentials
    
            else:
                        return render(request,'Login.html')

    # No backend authenticated the credentials
    

        return render(request,'Login.html')
def LogoutUser(request):
    logout(request)
    return render(request,'Login.html') 
    