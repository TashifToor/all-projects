from django.shortcuts import render
from .models import Student,Subject,Result
from .serializers import StudentSerializers,SubjectSerializers,ResultSerializers
from rest_framework import viewsets

class StrudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    
class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializers

class ResultViewSet(viewsets.ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=ResultSerializers        

# Create your views here.
