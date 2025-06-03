from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .models import Studnet
from .serializers import StudentSerialzier
import hashlib

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Studnet.objects.all()
    serializer_class=StudentSerialzier
    def list(self,request,*args, **kwargs):
        cache_key='student_list_cache'
        data=cache.get(cache_key)
        if data is not None:
            return Response(data)
        queryset=self.get_queryset()
        serialzier=self.get_serializer(queryset,many=True)
        data=serialzier.data
        cache.set(cache_key,data,timeout=60*5)
        return Response(data)
    def retrieve(self, request, *args, **kwargs):
        cache.clear()
        return super().retrieve(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        cache.clear()
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        cache.clear()
        return super().destroy(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)        
        
        
        
        


# Create your views here.
