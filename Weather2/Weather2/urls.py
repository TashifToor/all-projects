from api import views
from django.contrib import admin
from django.urls import path,include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('w/',views.WeatherableAPI.as_view()),

]
