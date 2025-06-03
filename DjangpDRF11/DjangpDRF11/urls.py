from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from api import views
#cretaing defult router

router=DefaultRouter()

#regester studentviewset with router

router.register('StudentViewset',views.StudentViewset,basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
]
