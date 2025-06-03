from django.contrib import admin
from django.urls import path
from son import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Contact',views.Contact,name='Contact'),
    path('About',views.About,name='About'),
    path('Trending',views.Trending,name='Trending'),
    path('NewArrival',views.NewArrival,name='NewArrival'),

]
    