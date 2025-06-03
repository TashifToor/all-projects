from student import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('studentapi',views.StrudentViewSet,basename='student'),
router.register('subjectapi',views.SubjectViewSet,basename='subject'),
router.register('resultapi',views.ResultViewSet,basename='result'),




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),
    path('',include(router.urls)),
]
