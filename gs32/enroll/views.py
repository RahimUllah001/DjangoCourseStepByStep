from django.shortcuts import render
from . forms import StudentRegisteration
# Create your views here.


def show_form_data(request):
    fm = StudentRegisteration()
    return render(request, 'enroll/userregisteration.html',{'form': fm})