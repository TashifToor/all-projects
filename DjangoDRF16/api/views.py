from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import viewsets
from .custompermissions import CustomPermission 
# Create your views here.
class StudentAPI(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[CustomPermission]
    