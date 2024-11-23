from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    fee = models.IntegerField()
    date = None     #as this is  inhirit from above but i have no need for the field here so i will do this 

class Teacher(CommonInfo):
    date = models.DateField()
    salary = models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField()       #here i have override the date field according to my need
    payment = models.IntegerField()     
