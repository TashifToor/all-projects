from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudenrtSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(requset):
    if requset.method=="POST":
        json_data=requset.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudenrtSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg','Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
            
            
            
        
