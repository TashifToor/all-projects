from rest_framework.routers import DefaultRouter
from api import views
from django.contrib import admin
from django.urls import path,include

router=DefaultRouter()
router.register('studentapi',views.Studentapi,basename='student')
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='restframework')),
]

from django.conf import settings
from django.conf.urls.static import static 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
