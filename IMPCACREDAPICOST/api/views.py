from django.shortcuts import render
from .models import Student
from .serializers import StudentSerialzier
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
import hashlib

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialzier
    
    def list(self,request,*args,**kwargs):
        #create a unique cache key for request
        cache_key='student_list_cache'
        #try to get data from cache key
        data=cache.get(cache_key)
        if data is not None:
            return Response(data)
        #if not fetch try to get data from DB
        queryset=self.get_queryset()
        serialzer=self.get_serializer(queryset,many=True)
        data=serialzer.data
        #store result i cache for future request
        cache.set(cache_key,data,timeout=60*5)#cache for for 5 minute
        return Response(data)
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        cache_key=f'student_retrieve_{instance.id}'
        data=cache.get(cache_key)
        if data is not None:
            return Response(data)
        serializer=self.get_serializer(instance)
        data=serializer.data
        cache.set(cache_key,data,timeout=60*3)
        return Response(data)
    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)    
    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs) 
        
