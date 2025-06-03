from django.shortcuts import render
from rest_framework import viewsets
from joe.models import Company,Employee
from joe.serializers import CompanySerializers,EmployeeSeraializers

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSeraializers    
    
    