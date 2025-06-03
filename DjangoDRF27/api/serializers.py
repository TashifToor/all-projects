from rest_framework import serializers
from .models import Singer,Song
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"

class SingerSerializer(serializers.ModelSerializer):
    song1=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields="__all__"
         
        
                
        