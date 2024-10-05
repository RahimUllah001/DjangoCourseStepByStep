from django.shortcuts import render
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect
# Create your views here.

def on_submission(request):
    return render(request,'enroll/success.html')
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            print("ye data post method k zareye aya hai:")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            return HttpResponseRedirect('/regi/formsubmitted')
            # return render(request,'enroll/success.html',{'name':name})  

    else:
        fm = StudentRegisteration()
        print("ab get method chala hai")
    return render(request,'enroll/userregisteration.html',{'form':fm})  
