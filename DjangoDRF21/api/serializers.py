from .models import Student
from rest_framework import serializers
class SrudentSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"