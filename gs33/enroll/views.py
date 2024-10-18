from django.shortcuts import render
from .forms import StudentRegisteration,TeacherRegisteration

# Create your views here.
def student_form(request):

    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            fm.save()    
    else:
        fm = StudentRegisteration()
    return render(request, 'enroll/student.html',{'form':fm})

# view for teacher
def teacher_form(request):

    if request.method == 'POST':
        fm = TeacherRegisteration(request.POST)
        if fm.is_valid():
            fm.save()    
    else:
        fm = TeacherRegisteration()
    return render(request, 'enroll/teacher.html',{'form':fm})