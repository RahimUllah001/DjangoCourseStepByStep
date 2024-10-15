from django.shortcuts import render
from .forms import StudentRegisteration
from .models import User

# Create your views here.

def showformdata(request):      
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
           #how to insert data 
            reg = User(name=nm,email=em,password=pw)
            reg.save()

            '''# how to update some specifice data 
            # reg = User(id =2,name=nm,email=em,password=pw)        #how to update some data 
            reg.save()
            '''

            '''     #how to delete data
            reg = User(id=2)
            reg.delete()
            '''
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html',{'form':fm})  

# //////////////////////////////////////////////////
'''
# code for updating record through instance method
def showformdata(request):      
    if request.method == 'POST':
        pi = User.objects.get(pk=1)
        fm = StudentRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegisteration()
    return render(request,'enroll/userregisteration.html',{'form':fm})  
'''


# important message regarding updateing
'''
In Django, when you use reg = User(name="nasir",email=em,password=pw) followed by reg.save(), it creates a new record in the database, even if there is already a record with the same name. This is because Django doesn't know to treat the name field as a unique identifier for updating existing records.

On the other hand, when you use reg = User(id=3, name=nm, email=em, password=pw) followed by reg.save(), Django updates the record with the specified id (primary key). This is because id is the default primary key field in Django models, which uniquely identifies each record. If a record with id=3 exists, it will be updated; otherwise, a new record will be created with that id.

if anyone want it must to update then he can use this way
from django.shortcuts import render
from enroll.models import User
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print("post done")

            # Try to find the user by name
            try:
                # Check if a user with the given name exists
                reg = User.objects.get(name=nm)
                # If the user exists, update their details
                reg.email = em
                reg.password = pw
                print("Record found. Updating existing user.")
            except ObjectDoesNotExist:
                # If the user does not exist, create a new one
                reg = User(name=nm, email=em, password=pw)
                print("No matching record found. Creating a new user.")
            
            # Save the record (whether it's a new user or an update)
            reg.save()

    else:
        fm = StudentRegisteration()

    return render(request, 'enroll/userregisteration.html', {'form': fm})

'''