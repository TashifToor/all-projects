from django.shortcuts import render
from datetime import datetime
from son.models import contact


# Create your views here.
def index(request):
    return render(request,'index.html')
def Contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        desc=request.POST.get('desc')
        
        Contact=contact(name=name,email=email,password=password,desc=desc,date=datetime.today())
        Contact.save()
        
    
        
    
    return render(request,'Contact.html')
def About(request):
    return render(request,'About.html')
def Trending(request):
    return render(request,'Trending.html')
def NewArrival(request):
    return render(request,'NewArrival.html')