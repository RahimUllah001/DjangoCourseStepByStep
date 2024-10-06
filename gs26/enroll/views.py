from django.shortcuts import render
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            print("form Validated")
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html',{'form':fm})  
