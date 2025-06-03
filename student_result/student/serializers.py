from .models import Student,Subject,Result
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields="__all__"
        
class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields="__all__"                 