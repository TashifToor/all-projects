from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    image=models.ImageField(upload_to='student_image/',null=True,blank=True)

# Create your models here.
