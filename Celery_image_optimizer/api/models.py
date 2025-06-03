from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    image=models.ImageField(upload_to='student_image/',blank=True,null=True)
#((blank)))This means the image field is optional in Django admin forms or serializers.
#Django will allow this field to be left blank in forms.
#((null)))This allows the database column to store NULL when no image is uploaded.
#It works with blank=True to make the field optional.



# Create your models here.
