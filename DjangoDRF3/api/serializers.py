from rest_framework import serializers
from .models import student

class StudenrtSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=99)
    
    def create(self,validate_data):
        return student.objects.create(**validate_data)
     