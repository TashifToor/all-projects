from django.db import models
class Singer(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title=models.CharField(max_length=100)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
    #This creates a foreign key field in the Song model. It establishes a many-to-one relationship, meaning:
    #This is the related model. It tells Django that this ForeignKey refers to the Singer model.
    #This defines what happens when a related Singer object is deleted:

#CASCADE means that if a Singer is deleted, all of their related Songs will also be deleted automatically.
    duration=models.IntegerField()
    
    def __str__(self):
        return self.title
        
# Create your models here.
