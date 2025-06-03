from django.shortcuts import render
from .models import Student
from .serializers import SrudentSerialzier
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter



# Create your views here.
class StudentApiView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=SrudentSerialzier#for each
    # filter_backends=[SearchFilter]#class
    # search_fields=['city']
    # search_fields=['passby']
    
    filter_backends=[OrderingFilter]
    ordering_fields=['name','city']
    