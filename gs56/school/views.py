from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.


def home(request):

    student_data = Student.objects.all()[:3]        #gives firsrt three
    student_data = Student.objects.all()[2:5]        #gives firsrt three
    student_data = Student.objects.all()[:7:2]        #gives from start to end with step 2
    context = {'students':student_data}
    print("SQL Querry: ",student_data.query)
    return render(request,'home.html', context) 
