from django.shortcuts import render
from .models import Student
# Create your views here.


def studentinfo(request):
    stud = Student.objects.all()

    return render(request,'enroll/studetails.html',{'stu':stud})


def single_stu_info(request):
    stud = Student.objects.get(pk=3)

    return render(request,'enroll/single_student_detail.html',{'stu':stud})