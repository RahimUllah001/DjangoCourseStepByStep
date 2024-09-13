from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def learn_django(request):
    return HttpResponse('Hello Djnago')


def learn_python(request):
    return HttpResponse('<h1>Hello Python<h1/>')

def learn_var(request):
    a = '<h1>Hello Python<h1/>'
    return HttpResponse(a)

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_format(request):
    a  = 'Geeky shows'
    return HttpResponse(f'Hello How are u{a}')
