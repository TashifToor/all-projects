from api import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router=DefaultRouter()
router.register('singerapi',views.SingerModelViewSets,basename='singer')
router.register('songapi',views.SongModelViewSets,basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path('auth',include('rest_framework.urls',namespace='rest_framework')),
]
