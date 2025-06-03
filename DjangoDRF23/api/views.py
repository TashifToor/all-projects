from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from .mylimmitofferpagination import mylimmitofferpagination



# Create your views here.
class StudentAPIVIEW(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers #offset mean is ke badd record dekhna chahta hui
    pagination_class=mylimmitofferpagination
    