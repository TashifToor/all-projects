from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    def start_with_a(value):
        if value[0].lower()!='a':
            raise serializers.ValidationError('name must start with a')
    name=serializers.CharField(validators=[start_with_a])    
        
    class Meta:
        model=Student
        fields='__all__'
        # read_only_fiels=['name','roll']
        # extra_kwargs={'name':{'read_only':True}}
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('SEATS ARE FULLS TRY LATER')
        return value
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='ali'and ct.lower()!='krachi':
            raise serializers.ValidationError('city name must be krachi')
        return data
    
    
            