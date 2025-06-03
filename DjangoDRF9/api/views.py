#generic apiview or m=ixixn

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

#list and create dont require pk
class StudentLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 
    
#retive,destroy,update require pk    
class StudebtRUD(GenericAPIView,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)    
    
        
        
       
