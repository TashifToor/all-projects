from .models import Weather
from rest_framework import serializers

class WeatherSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields="__all__"