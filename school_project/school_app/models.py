from django.db import models
from django.contrib.auth.models import User,AbstractUser



# Create your models here.



class Teacher(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Phone_no=models.CharField(max_length=12)
    user_type=models.CharField(max_length=10)
    value=models.IntegerField(max_length=1)
    Username=models.CharField(max_length=12,default='Teacher')
    Password=models.CharField(max_length=8,default=786)
    Subject=models.CharField(max_length=21,default='maths')

class Student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    GENDER_CHOICES= (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Address=models.CharField(max_length=50)
    Phone_no=models.CharField(max_length=12)
    user_type=models.CharField(max_length=10)
    value=models.IntegerField(max_length=1)
    Username=models.CharField(max_length=12,default='student')
    Password=models.CharField(max_length=8,default=788904)
    cls=models.CharField(max_length=5,default=0)



