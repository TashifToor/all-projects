from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
#authentications
from rest_framework.authentication import BasicAuthentication
#permisssion
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


class StudentModelViewSets(viewsets.ModelViewSet):
# class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #check seeting bottom
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    permission_classes=[AllowAny]#use for those api that dont require auyh
    permission_classes=[IsAdminUser]#only few user acces it

    
# class StudentModelViewSets2(viewsets.ModelViewSet):
# # class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     #check seeting bottom
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated,AllowAny]#for those api who dont require authentication
# class StudentModelViewSets3(viewsets.ModelViewSet):
# # class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     #check seeting bottom
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated]        
