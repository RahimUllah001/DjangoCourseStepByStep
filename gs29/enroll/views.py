from django.shortcuts import render
from enroll.models import User
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect
# Create your views here.

def showformdata(request):      
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print("post done")
            
            # how to insert data into database
            reg = User(name=nm,email=em,password=pw)            #this line is for insertion into database
            reg.save()

            '''
            # how to update
            reg = User(id=3,name=nm,email=em,password=pw)     #if we write specific id then this will work fot updating some record in db
            reg.save()      #actully this function do all the above work i.e insert and update
            '''

            '''
            # how to delete
            reg = User(id = 10)
            reg.delete()
            '''
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html',{'form':fm})  
