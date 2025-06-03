from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} ({self.rollno})"

class Subject(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} ({self.code})"

class Result(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()        
    def __str__(self):
        return f"{self.student} - {self.subject}: ({self.marks})"
    
    
