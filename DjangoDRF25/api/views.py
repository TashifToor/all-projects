from django.shortcuts import render
from .models import Singer,Song
from rest_framework import viewsets
from .serializers import SingerSerializers,SongSerializers

class SingerViewSets(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializers
class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializers 
# Create your views here.
