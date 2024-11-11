from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # students_data = Student.objects.get(pk=3)       #to take data using any key which is once in db
    
    # students_data = Student.objects.first()     #to take first data from db
    # students_data = Student.objects.last()     #to take lastt data from db
    
    # students_data = Student.objects.latest('pass_date')     #to take latest data from db based on the given field
    # students_data = Student.objects.earliest('pass_date')     #to take earliest data from db based on the given field
    
    # students_data = Student.objects.all()     #to take earliest data from db based on the given field
    # print("Student data:", students_data.exists())       #Student: data True
    
    # students_data = Student.objects.create(name='ummehani',roll=999,city='bannu',marks=100,pass_date='2020-5-6')      #giving values to coloumns
    # students_data = Student.objects.get_or_create(name='ummehani',roll=999,city='bannu',marks=100,pass_date='2020-5-6')     #if exist then get else create the new one 
    # students_data = Student.objects.filter(id=10).update(name='ummehaniwazir',roll=888,)     #Updating one record
    # students_data = Student.objects.filter(marks=100).update(city='prizeholder')      #Updating many  record
    # students_data,created = Student.objects.update_or_create(city='swat', defaults={'city':'Bannu'})      #Updating many  record
    # students_data, created = Student.objects.update_or_create(city='swat',  defaults={'city': 'Bannu', 'roll': 123,      'marks':2000,'pass_date':'2020-5-6'})        #creating records if not 3xist
    
    # Creating multiple objects at once
    """
     objs = [
            Student(name='Umer1',roll = 1111, city='Peshawar',marks = 999, pass_date = '2020-5-6'),
            Student(name='Umer2',roll = 1112, city='Peshawar',marks = 999, pass_date = '2020-5-6'),
            Student(name='Umer3',roll = 1113, city='Peshawar',marks = 999, pass_date = '2020-5-6'),
        ]

    students_data = Student.objects.bulk_create(objs)
    """
    # students_data = Student.objects.filter(pk=10).delete()        #for deletig
    # students_data = Student.objects.all().delete()        #for deletig

    # For couting total item s of db
    students_data = Student.objects.all()
    print("Student data:", students_data.count())  
    


   
    print("Student data:", students_data)       #Student: data True
    
    return render(request,'school/home.html', {'student':students_data})  