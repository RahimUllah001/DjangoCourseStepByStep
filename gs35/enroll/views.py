from django.shortcuts import render
from .forms import StudentRegisteration

from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)  
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Now u can login.')
            print("message level: ",messages.get_level(request))
            messages.debug(request,"this is debug")
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,"this is new debug")
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html', {'form':fm})


