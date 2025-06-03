from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# @api_view()

# # Create your views here.

# def helloworld(request):
#     return Response({'msg',"Hello World "})

@api_view(['GET','POST'])
def helloworld(request):
    if request.method=='GET':
       
        return Response({'msg':'this is get request'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'this is post request','data':request.data}) 
