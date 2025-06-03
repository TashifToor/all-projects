from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    # print(stu)
    serializers=StudentSerializer(stu)
    # print(serializers)
    # print(serializers.data)
    json=JSONRenderer().render(serializers.data)
    # return JsonResponse(serializers.data)
    # print(json)
    return HttpResponse(json,content_type='application/json') 


def student_list(request):
    stu=Student.objects.all()
    # print(stu)
    serializers=StudentSerializer(stu,many=True)
    # print(serializers)
    # print(serializers.data)
    json=JSONRenderer().render(serializers.data)#..
    # # print(json)
    return HttpResponse(json,content_type='application/json') #..
    # return JsonResponse(serializers.data,safe=False)just one line