from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def fee_django(request):
    return HttpResponse(3000)

def fee_python(request):
    return HttpResponse(2000)