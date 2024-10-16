from django.shortcuts import render

# Create your views here.

def home(request, check):
    print(check)
    return render(request,'enroll/home.html')       #also we can pass the above check to template usong dictionary or contaxt 

def show_details(request,my_id=1):      #setting default values for my_id =1 
    if my_id < 15:
        student  = {'id' : my_id ,"age_Category": "bachay"}
        
    if my_id > 15:
        student  = {'id' : my_id ,'age_Category': "young"}
        
    if my_id > 50:
        student  = {'id' : my_id ,"age_Category": "buzarg"}

    return render(request, 'enroll/show.html',student)        #yaha key waha html mai vraible hotha haikkk
    

# the below is for such urls http://127.0.0.1:8000/student/4/1/

def show_subdetails(request, my_id, my_subid):
    if my_id > 1 and my_subid < 15 :
        student  = {'id' : my_id ,"age_Category": "bachay", 'info':'sub detail'}
        
    if my_id > 15 and my_subid < 60:
        student  = {'id' : my_id ,'age_Category': "young", 'info':'sub detail'}
        
    if my_id > 60 and my_subid < 1000:
        student  = {'id' : my_id ,"age_Category": "buzarg", 'info':'sub detail'}
    

    return render(request, 'enroll/show.html',student)        #yaha key waha html mai vraible hotha haikkk
  