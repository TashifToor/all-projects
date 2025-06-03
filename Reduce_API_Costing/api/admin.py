from django.contrib import admin
from .models import Studnet
@admin.register(Studnet)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','image']

# Register your models here.
