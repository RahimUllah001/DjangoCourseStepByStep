from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.


def home(request):

    student_data = Student.objects.filter(Q(id=4) & Q(roll=104))        #using and opeeration
    student_data = Student.objects.filter(Q(id=4) | Q(roll=105))        #using OR operations 
    student_data = Student.objects.filter(~Q(id=4))        #using Negation operations ==> All except having id = 4

    context = {'students':student_data}
    return render(request,'home.html', context) 