from django.shortcuts import render
from .models import Student
# Create your views here.


def home(request):
    # student_data = Student.students.all()     # thiss si valid when i use the custom manageer manager==>   students = CustomManager()

    # student_data = Student.objects.all()      #thiss si valid when i use the default manager which always used in model.py if we nor specify ==>    objects = models.Manager()

    student_data = Student.students.get_stu_roll_range(112,114)     # this is valid when i use the custom manager with custom method  ==>   students = CustomManager()


    return render(request,'school/home.html',{'students':student_data})