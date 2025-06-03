from django.urls import path
from .views import Weather_APIVIEW

urlpatterns = [
    path('weather/', Weather_APIVIEW.as_view(), name='weather'),
]
