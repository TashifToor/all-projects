from django.shortcuts import render
from .models import Student
from .serializers import SrudentSerialzier
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
class StudentApiView(ListAPIView):
    queryset=Student.objects.all()
    # queryset=Student.objects.filter(passby='user2')
    serializer_class=SrudentSerialzier#for each
    filter_backends=[DjangoFilterBackend]#class
    filterset_fields=['passby','name']
    # filterset_fields=['passby','city ]#for globaly
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    
    
    