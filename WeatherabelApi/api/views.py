from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerialzier
from rest_framework.response import Response
import requests


class Weather_APIVIEW(APIView):
    def get(self,request):
        city=request.GET.get('city')
        if not city:
            return Response({'error':'city parameter is requiured'}, status=status.HTTP_400_BAD_REQUEST)
        api_key="3cbef0baa21ce87e012d29f49f7c4df8"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response=requests.get(url)
        if response.status_code!=200:
            return Response({'error':'city parameter is require'},status=status.HTTP_400_BAD_REQUEST)
        data=response.json()
        Weather_data={
            'city':city,
            'temprature':data['main']['temp'],
            'description':data['weather'][0]['description'],
            'humidity':data['main']['humidity']
        }
        weather_obj=Weather.objects.create(**Weather_data)#creating Database
        serialzier=WeatherSerialzier(weather_obj)
        return Response(serialzier.data,status=status.HTTP_200_OK)
        

# Create your views here.
