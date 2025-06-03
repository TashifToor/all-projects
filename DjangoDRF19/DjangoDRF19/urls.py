# from api import views
# from rest_framework.routers import DefaultRouter
# from django.contrib import admin
# from django.urls import path,include

# router=DefaultRouter()
# router.register('studentapi',views.StudentModelViewSet,basename='student')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/',include('rest_framework.urls',namespace='rest_fraamework')),
#     path("",include(router.urls)),
# ]
from django.urls import path,include
from api import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuapi/',views.StudentListView.as_view()),
    # path('stuapi/',views.StudentCreateView.as_view()),
    path('stuapi/<int:pk>',views.StudentRetrieveView.as_view()),
#     path('stuapi/<int:pk>',views.StudentUpdateView.as_view()),
#     path('stuapi/<int:pk>',views.StudentDestroyView.as_view()),
]