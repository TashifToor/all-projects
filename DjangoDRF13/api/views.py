from django.shortcuts import render
from .models import Student
from .serializer import StudentSerialzier
from  rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from rest_framework import viewsets


# Create your views here.
class StudentModelViewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialzier
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]2nd user give password for only read only super user can do all crud
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]#only give read witho=ut password if 2nd user type wpassword it can do erverything
    permission_classes=[DjangoObjectPermissions]