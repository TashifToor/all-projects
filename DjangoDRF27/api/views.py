from django.shortcuts import render
from .models import Song,Singer
from .serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets

class SingerModelViewSets(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
class SongModelViewSets(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
