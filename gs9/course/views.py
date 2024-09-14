from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    coursename = {'cname':'Djnagoo'}
    return render(request, 'course/courseone.html',context=coursename)      #pasing data through context or instead of ''''context=coursename''' we can only write coursename

def learn_python(request):
    coursename = {'cname':'PYthon'}
    return render(request, 'course/courseone.html', {'cname':'PYthon'})     #passing data asa dictionary
