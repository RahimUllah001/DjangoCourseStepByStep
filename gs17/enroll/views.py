from django.shortcuts import render
from .models import Student
# Create your views here.

# to get  data of all student from database 

def studentinfo(request):
    stud = Student.objects.all()

    return render(request,'enroll/studetails.html',{'stu':stud})

# to get  data of singl student from database 
def single_stu_info(request):
    stud = Student.objects.get(pk=3)

    return render(request,'enroll/single_student_detail.html',{'stu':stud})