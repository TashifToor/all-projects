from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def studentapi(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.object.get(id=id)
            serializers=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializers)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializers=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializers.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializers=StudentSerializer(data=pythondata)
        if serializers.is_valid():
            serializers.save()
            res={'msg':'DATA CREATED'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
        
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializers=StudentSerializer(stu,data=pythondata,partial=True)
        if serializers.is_valid():
            serializers.save()
            res={'msg':'DATA UPDATED'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')    
        
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg','DATA DELETED'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')    
        
             
        