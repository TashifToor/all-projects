from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from .customauthentication import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]