from django.contrib import admin
from .models import Weather
@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display=['id','city','temprature','description','humidity']

# Register your models here.
