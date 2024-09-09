from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return HttpResponse('learn django with us ')