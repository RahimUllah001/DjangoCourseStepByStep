from django.shortcuts import render
from .forms import StudentRegisteration
# Create your views here.

def showformdata(request):
    fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html',{'form':fm})