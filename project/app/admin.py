from django.contrib import admin
from .models import AadharModel,StudentModel

# Register your models here.(
@admin.register(AadharModel)
class Aadharadmin(admin.ModelAdmin):
    list_display=['id','Aadhar_no']


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_Name','Aadhar_no']    
