from django.db import models
class Weather(models.Model):
    city=models.CharField(max_length=250)
    temprature=models.FloatField()
    description=models.CharField(max_length=250)
    humidity=models.IntegerField()
    create_at=models.DateField(auto_now_add=True)

# Create your models here.
