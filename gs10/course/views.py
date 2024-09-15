from django.shortcuts import render
from datetime import datetime
# Create your views here.

def learn_django(request):
    cname = 'Django'
    duration = '4 Months'

    seats = 10
    django_Details = {'n':cname,'du':duration,'st':seats}

    return render(request,'course/courseone.html',context=django_Details)

def learn_python(request):
    return render(request,'course/coursetwo_with_filter.html',{'nm':'this course iMMMMMMMs awesome'})


def showing_date_time_template(request):
    d = datetime.now()

    return render(request,'course/date_time_template.html',{'dt':d}) 

def filter_for_float__number_format(request):
    return render(request,'course/float_number_formate.html',{'p1':56.24321, 'p2':56.0000, 'p3':56.37000}) 

def if_st(request):
    # return render(request,'course/if_st.html',{'name':'True'}) #will not show anything if we pass false value
    # return render(request,'course/if_st.html',{'name':'Django'})
    # return render(request,'course/if_st.html',{'name':'Django', 'st':5})
    return render(request,'course/if_st.html',{'name':'Django',})

def loops(request):
    student = {'names': ['rahim','nasir','ibrahim']}
    return render(request,'course/for_loop.html',context = student)

def forloop_varaibles(request):
    student = {'names': ['rahim','nasir','ibrahimend']}

    return render(request,'course/forloop_varaibles.html',student)

def nested_loop_and_dict(request):
    stu = { 'stu1' : {'name': "rahim",'age':1},
            'stu2' : {'name': "israr",'age':2},
            'stu3' : {'name': "faizan",'age':3},

          }
    
    students = {'student': stu}
    
    return render(request,'course/nested_dict_and_for.html',students)
   

def passing_key_value(request):
    data = { 'stu1' : {'name': "rahim",'age':1},
                'stu2' : {'name': "israr",'age':2},
                'stu3' : {'name': "faizan",'age':3},

            }
    
    return render(request,'course/nested_dict_and_for.html',{'data':data})
    