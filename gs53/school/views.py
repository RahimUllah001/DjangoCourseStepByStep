from django.shortcuts import render
from .models import Student
from datetime import date,time
# Create your views here.


def home(request):
    # student_data = Student.objects.all()
   
    # student_data = Student.objects.filter(name__exact='rahim')        #Exact=rahim ==> Case sensitive
    # student_data = Student.objects.filter(name__iexact='rahim')        #iexact=rahim ==> Case in-sensitive ||Sqlquerry ==> Select *  FROM "school_student" WHERE "school_student"."name" LIKE rahim ESCAPE '\'
   
    # student_data = Student.objects.filter(name__istartswith='r')        #name__istartswith=r ==> name starts with s but in casesensitive ==>in-casesensitive  ||Sqlquerry ==> Select * FROM "school_student" WHERE "school_student"."name" LIKE r% ESCAPE '\'
    # student_data = Student.objects.filter(name__iendswith='m')        #name__istartswith=r ==> name ends with m but in casesensitive ==>in-casesensitive  ||Sqlquerry ==> Select * FROM "school_student" WHERE "school_student"."name" LIKE %r ESCAPE '\'
    # student_data = Student.objects.filter(name__contains='r')        #name__contains=r ==> alone r or inbetween or on side of other string  ||Sqlquerry ==> Select * FROM "school_student" WHERE "school_student"."name" LIKE %r% ESCAPE '\'
    # student_data = Student.objects.filter(name__icontains='r')        #name__contains=r ==> alone r or inbetween or on side of other string ==>in-casesensitive  ||Sqlquerry ==> Select * FROM "school_student" WHERE "school_student"."name" LIKE %r% ESCAPE '\'
    
    # student_data = Student.objects.filter(id__in=[2,4])     #FROM "school_student" WHERE "school_student"."id" IN (2, 4)
   
    # student_data = Student.objects.filter(id__gt=2)     #FROM "school_student" WHERE "school_student"."id" > 2
    # student_data = Student.objects.filter(id__gte=2)     #FROM "school_student" WHERE "school_student"."id" >= 2
    # student_data = Student.objects.filter(id__lte=2)     #FROM "school_student" WHERE "school_student"."id" <= 2
    
    # student_data = Student.objects.filter(id__range=(2,5))     #FROM "school_student" WHERE "school_student"."id" BETWEEN 2 AND 5
    
    # student_data = Student.objects.filter(admdatetime__date=date(2024,10,8))     #FROM "school_student" WHERE django_datetime_cast_date("school_student"."admdatetime", Asia/Kolkata, UTC) = 2024-10-08
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2024,10,7))     #FROM "school_student"WHERE django_datetime_cast_date("school_student"."admdatetime", Asia/Kolkata, UTC) > 2024-10-07
    
    # student_data = Student.objects.filter(admdatetime__time=time(11,18))     #FROM "school_student" WHERE django_datetime_cast_time("school_student"."admdatetime", Asia/Kolkata, UTC) > 10:00:00
    # student_data = Student.objects.filter(admdatetime__time__gt=time(10,00))     #FROM "school_student" WHERE django_datetime_cast_time("school_student"."admdatetime", Asia/Kolkata, UTC) > 10:00:00
    student_data = Student.objects.filter(roll__isnull=True)
    
    print("Return",student_data)
    print()     #fror new line
    print("Return",student_data.query)

    return render(request,'home.html', {'students':student_data}) 