from django.shortcuts import render
from .forms import StudentRegisteration
# Create your views here.

def showformdata(request):
    fm = StudentRegisteration(auto_id=True, label_suffix=" ", initial= {'name': 'rahim'})
    return render(request,'enroll/userregisteration.html',{'form':fm})