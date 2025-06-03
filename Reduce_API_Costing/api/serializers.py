from .models import Studnet
from rest_framework import serializers

class StudentSerialzier(serializers.ModelSerializer):
    class Meta:
        model=Studnet
        fields="__all__" 