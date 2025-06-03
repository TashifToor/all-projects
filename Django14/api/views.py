from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST','PUT','PATCH','DELETE'])

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

# Create your views here.
def studentapi(request,pk=None):
    if request.method=="GET":
        id=pk
        # id= request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
        
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA CREATED'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    if request.method=="PUT":
        id=pk
        # id=request.data.get("id")
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'COMPLETE DATA UPDTAED'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="PATCH":
        id=pk
        # id=request.data.get("id")
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'PARTIAL DATA UPDTAED'})
        return Response(serializer.errors)
    
    
    if request.method=="DELETE":
        id=pk
        # id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'DATA DELETED'})
    
        
    
    