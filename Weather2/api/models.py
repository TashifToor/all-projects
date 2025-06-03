from django.db import models
class Weather(models.Model):
    city=models.CharField(max_length=50)
    temprature=models.FloatField()
    description=models.CharField(max_length=1000)
    humidity=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
