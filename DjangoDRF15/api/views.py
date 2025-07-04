from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import viewsets
# Create your views here.
class StudentAPI(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    
    
