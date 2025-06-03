from rest_framework import serializers
from joe.models import Company,Employee


class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
         model=Company
         fields="__all__"
    
        
           
    
        
            
            
         #hyperlink is use for url that came in output a clickable url
          
        #for all field __alt__ is use and field tell which field show in JSON output for PUT,GET

        
class EmployeeSeraializers(serializers.HyperlinkedModelSerializer):
    employee_id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"  

        

              
    