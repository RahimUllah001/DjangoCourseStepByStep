from django.db import models

# Create your models here. Always after creating class we have always to register it 
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70) 