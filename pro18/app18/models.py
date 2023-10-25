from django.db import models

class Student(models.Model):
  
    name=models.CharField(max_length=30)
    contactnumber=models.IntegerField()
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=50)
    nameofparent=models.CharField(max_length=50)
    aadhaarno=models.IntegerField()
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    permanentaddress=models.CharField(max_length=40)
    payamount=models.IntegerField()
    course=models.CharField(max_length=50)
  
    
    class Meta:
        db_table="std"


    def __str__(s):
        return s.name

class College(models.Model):
    srno=models.IntegerField()
    collegename=models.CharField(max_length=40)
    departmentname=models.CharField(max_length=40)
    subject1=models.CharField(max_length=40)
    subject2=models.CharField(max_length=40)
    subject3=models.CharField(max_length=40)
    
    
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    #it is only use for delete

    class Meta:
        db_table="clg"

# Create your models here.


# Create your models here.
