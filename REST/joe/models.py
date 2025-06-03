from django.db import models

# Create your models here.
#creating company model

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)#compant is is just variable autofield is main that automatically craeates unique and autoincremanting primary key
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=40,choices=(("IT","IT"),#choices can be put anywhere on the field
                         ("NON-IT","NON-IT"),
                         ("MOBILE-USER","MOBILE-USER")))
    added_data=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    


#creating employee model

class Employee(models.Model):
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=70)
    About=models.TextField()
    position=models.CharField(max_length=111,choices=(("IT LEADER","IT LEADER"),
                             ("Project Manager","Project Manager"),
                             ("Software ENgineer","Software Engineer") ))    

company=models.ForeignKey(Company,on_delete=models.CASCADE) 


#each one id deine belows
#company is just the field of name
# (Company, ... ):
# The first argument passed to ForeignKey is the model it's pointing to — here, it's linking to the Company model. This means each employee is assigned to one company.

# on_delete=models.CASCADE:
# This tells Django what to do if the linked Company is deleted.

# on_delete is a parameter.

# models.CASCADE means if the company is deleted, the employee will also be deleted (cascading delete).
#foreign key:    A  field type that creates a link to another model (a "foreign key" in database terms). It’s used to connect two tables — in this case, Employee connects to Company.   