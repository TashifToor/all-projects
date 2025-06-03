from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from api import views

router=DefaultRouter()
# router.register('Studentapi',views.StudentReadOnlyModelViewSets,basename='student')
router.register('Studentapi',views.StudentModelViewSets,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
