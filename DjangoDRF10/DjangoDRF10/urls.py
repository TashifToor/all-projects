"""
URL configuration for DjangoDRF10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('sapi/',views.StudentList.as_view()),
    # path('sapi/',views.StudentCreate.as_view()),
    # path('sapi/<int:pk>',views.StudentReterive.as_view()),
    # path('sapi/<int:pk>',views.StudentUpdate.as_view()),
    # path('sapi/<int:pk>',views.StudentDestroy.as_view()),
    # path('sapi/',views.StudentLC.as_view()),
    # path('sapi/<int:pk>',views.StudentRU.as_view()),
    # path('sapi/<int:pk>',views.StudentRD.as_view()),
    path('sapi/<int:pk>',views.StudentRUD.as_view()),
    
]
