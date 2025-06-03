from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from api.throttling import JackRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     authentication_classes=[SessionAuthentication]
#     # permission_classes=[IsAuthenticatedOrReadOnly]
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     throttle_classes=[AnonRateThrottle,JackRateThrottle]
    
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
class StudentRetrieveView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    
class StudentCreateView(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

class StudentDestroyView(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

class StudentUpdateView(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

                    
    

