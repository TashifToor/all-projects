from django.contrib import admin
from .models import Subject,Student,Result
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['id','name','code']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=['id','student','subject','marks']        

# Register your models here.
