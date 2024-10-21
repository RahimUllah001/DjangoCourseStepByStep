from django.shortcuts import render
from .forms import signUpForm
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm = signUpForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request,'Account created successfully')
    else:
        fm = signUpForm()
    return render(request,'enroll/signup.html', {'form':fm})