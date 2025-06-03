from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser 
from .models import Student
from .serializers import StudentSeriializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.

def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        
        if id is not None:
           stu=Student.objects.get(id=id)
           serializer=StudentSeriializer(stu)
           json_data=JSONRenderer().render(serializer.data)
           return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()    
        serializer=StudentSeriializer(stu)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSeriializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='applications/json')
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='applications/json')
    
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        #if we remove partial =true then it want all value in database like inap.py 
        # i dont prove roll no and it still runnig if we remove then we have to put roll no and all data 
        serializer=StudentSeriializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'mes':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'DELETED'}
        # json_data=JSONRenderer.render(res)
        # return HttpResponse(json_data,content_type='application/json')
            
            
                
    
        
    
        