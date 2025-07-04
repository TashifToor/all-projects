
from.models import Student
from rest_framework import serializers

#validator

def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('name stat with r')
    
        

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
   
        
    
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
   
    
    
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    
     #field level validations   
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('seat full')
        return value
    #object leevel validationm
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='ali' and ct.lower()!='krachi':
            raise serializers.ValidationError('ct must be krachi')
        return data
        
    

        
        