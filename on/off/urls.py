from django.contrib import admin
from django.urls import path
from off import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Loginuser,name='login'),
    path('Logout',views.Logoutuser,name='logout'),

]
