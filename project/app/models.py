from django.db import models


class AadharModel(models.Model):
    Aadhar_no=models.IntegerField()
    def __str__(self):
        return str(self.Aadhar_no)

# Create your models here.
class StudentModel(models.Model):
    stu_Name=models.CharField(max_length=50)
    stu_Email=models.EmailField()
    stu_Contact=models.IntegerField()
    Aadhar_no=models.OneToOneField(AadharModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.stu_Name
