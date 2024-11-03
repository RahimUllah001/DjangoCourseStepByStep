from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Student,Teacher
from django.db.models import Q
# Create your views here.

def home(request):
    # students_data = Student.objects.all()       #by this command : students_data.query:  we can find the actual sql query behind this ==>SELECT "school_student"."id", "school_student"."name", "school_student"."roll", "school_student"."city", "school_student"."marks", "school_student"."pass_date" FROM "school_student"
   
    # students_data = Student.objects.filter(marks=77)        #SELECT * from school_student WHERE school_student.marks = 100
    # students_data = Student.objects.filter(city = "Peshawar")        #SELECT * from school_student WHERE school_student. = "Peshawar"
    # students_data = Student.objects.filter(pass_date = "2024-10-06")        #SELECT * from school_student WHERE school_student.pass_date = "2024-10-06";
    # students_data = Student.objects.exclude(pass_date = "2024-10-06")        #SELECT * from school_student WHERE NOT ("school_student"."pass_date" = 2024-10-06)
   
    # students_data = Student.objects.order_by('pass_date')        #SELECT * from school_student  ORDER BY "school_student"."pass_date" ASC
    # students_data = Student.objects.order_by('-pass_date')        #SELECT * from school_student  ORDER BY "school_student"."pass_date" DESC
    # students_data = Student.objects.order_by('?')        #SELECT * from school_student   ORDER BY random() ASC
    # students_data = Student.objects.order_by(Lower('name'))        #SELECT * from school_student   ORDER BY LOWER("school_student"."name") ASC ==> it is case-insensitive because the LOWER() function is being applied. We use this when their is some name stats from lower while some stats from upper
    # students_data = Student.objects.order_by('id').reverse()[:6]       #SELECT * from school_student   ORDER BY "school_student"."id" DESC LIMIT 6
    # students_data = Student.objects.values()      #SELECT * from school_student
    # Namedtuple ==> Such tuple which we can retieve through name rather than index which actually he is i.e student.name rather than student.[0]
    # students_data = Student.objects.values('name','marks')      #SELECT "name", "marks" FROM "school_student"
    # students_data = Student.objects.values_list('id','name',named=True)      #SELECT "school_student"."id", "school_student"."name" FROM "school_student" Student data <QuerySet [Row(id=1, name='Rahim'), Row(id=2, name='nasir'), etc etc 
    # students_data = Student.objects.using('default')      #SELECT * from school_student  ==> it will use the default db wwhich always set in setting.py file
    qs1 = Student.objects.values_list('id','name',named=True)
    qs2 = Teacher.objects.values_list('id','name',named=True)
    students_data = qs2.union(qs1)      #here it will remove the duplicate of two querries 

    # students_data = qs2.union(qs1,all=True)     #here duplicate is allowed
    # students_data = qs2.intersection(qs1)     #It will give intersection of two queries
    # students_data = qs2.difference(qs1)     #It will give that data of qs2 which is not common with qs1
    # students_data = qs2.difference(qs1)     #It will give that data of qs2 which is not common with qs1


    #### AND OR OPERATOR###
    # students_data = Student.objects.filter(id=1) & Student.objects.filter(roll=112)    #Select * from school_student WHERE id = 1 AND roll = 112)
    # students_data = Student.objects.filter(Q(id=1) & Q(roll=112) )   #Select * from school_student WHERE id = 1 AND roll = 112) mean same to above 
    students_data = Student.objects.filter(Q(id=6) | Q(roll=112) )   #Select * from school_student WHERE id = 1 OR roll = 112) mean same to above 
 




    print("sql Querry", students_data.query)        #SELECT "id", "name"  FROM "school_student" UNION SELECT "id" ,"name" FROM "school_teacher"
    print("Student data", students_data)
    return render(request,'school/home.html', {'students':students_data})  
