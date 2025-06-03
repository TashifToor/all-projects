from django.shortcuts import render
from  .models import Student
from .serializers import StudentSerialzier
from rest_framework import viewsets

class Studentapi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialzier

# Create your views here.
