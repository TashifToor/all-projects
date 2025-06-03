from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


# Create your views here.
class StudentViewset(viewsets.ViewSet):
    def get(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serialzier=StudentSerializer(stu)
            return Response(serialzier.data)
    def create(self,request):
        serializer=StudentSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA CREATED'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA UPDATED'},status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA UPDATED'},status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def destroy(request,self,pk):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'DATA DELETED'})
            
           
