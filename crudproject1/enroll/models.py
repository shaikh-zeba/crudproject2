from django.db import models

class User(models.Model):
    name=models.CharField(max_length=40)
    rollno=models.IntegerField()
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    
   
    
    
    

# Create your models here.
