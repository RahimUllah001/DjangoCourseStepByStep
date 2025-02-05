from django.shortcuts import render
from .models import Student
from django.db.models import Avg,Min,Max,Sum,Count
# Create your views here.


def home(request):
    
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    maximum = student_data.aggregate(Max('marks'))
    minimum = student_data.aggregate(Min('marks'))
    sum = student_data.aggregate(Sum('marks'))
    count = student_data.aggregate(Count('marks'))
    
    print(average)

    # print("Return",student_data.query)
    context = {'students':student_data,'average':average,'min':minimum,'max':maximum,'sum':sum,'count':count}

    return render(request,'home.html', context)