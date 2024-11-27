from django.db import models

# Create your models here.
# Proxy inhirentece ==> it meeans that we have one table in db but for with ane s it will show differnt behavius for  origanl and proxy
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True