from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from .mypagination import Mypagenumberpagnition


# Create your views here.
class StudentAPIVIEW(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers 
    pagination_class=Mypagenumberpagnition
    