from django.shortcuts import render
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests

class WeatherableAPI(APIView):
    def get(self,request):
        city=request.GET.get('city')
        if not city:
            return Response({'error':'city parameter is required'},status=status.HTTP_400_BAD_REQUEST)
        api_key="4fc1225097dadf6dea77e0c0121b82df"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
       
        response=requests.get(url)
        if response.status_code!=200:
            return Response({'error':'city parameter is require'},status=status.HTTP_400_BAD_REQUEST)
        data=response.json()
        Weather_data={
            'city':city,
            'temprature':data['main']['temp'],
            'description':data['weather'][0]['description'],
            'humidity':data['main']['humidity'],
            
        }
        weather_obj=Weather.objects.create(**Weather_data)
        serialzier=WeatherSerializer(weather_obj)
        return Response(serialzier.data,status=status.HTTP_200_OK)
        
        
        


# Create your views here.
