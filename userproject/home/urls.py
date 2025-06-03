from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Login',views.LoginUser,name='Login'),
    path('Logout',views.LogoutUser,name='Logout'),
    
]
