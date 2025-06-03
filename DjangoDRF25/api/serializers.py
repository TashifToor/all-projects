from .models import Singer,Song
from rest_framework import serializers
class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields="__all__"
class SingerSerializers(serializers.ModelSerializer):
    
    # song=serializers.StringRelatedField(many=True,read_only=True)((song name))
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)#((song id ))
    # song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')((creates link))
    # song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')#we also duration
    song=serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model=Singer
        fields="__all__"         
