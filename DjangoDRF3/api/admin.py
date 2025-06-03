from django.contrib import admin
from .models import student
@admin.register(student)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
    
    
