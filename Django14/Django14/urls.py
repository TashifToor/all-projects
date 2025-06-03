from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sapi/',views.studentapi),
    path('sapi/<int:pk>',views.studentapi),
]
