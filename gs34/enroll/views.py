from django.shortcuts import render
from .forms import StudentRegisteration

from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)  
        if fm.is_valid():
            fm.save()
            # how to write message in view
            messages.add_message(request,messages.SUCCESS,'Your Account has been created succeefully')
            # Alternatively, you can use the shortcut method:
            messages.info(request, 'Now u can login.')
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html', {'form':fm})


