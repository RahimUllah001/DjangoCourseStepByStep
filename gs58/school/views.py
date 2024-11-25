from django.shortcuts import render
from .models import Student,ExamCenter
# Create your views here.


def home(request):
    student_data = Student.objects.all()
    exam_center = ExamCenter.objects.all()
    print()
    context = {'students':student_data,'Examcenter':exam_center}
    return render(request,'school/home.html',context)