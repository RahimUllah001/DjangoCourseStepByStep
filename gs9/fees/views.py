from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def fee_django(request):
    cname = 'Django'
    duration  = '4 months'
    fees = 10000
    django_details = {'n':cname,'du':duration,'fee':fees}
    return render(request, 'fees/feesone.html',context=django_details)

def fee_python(request):
    return render(request, 'fees/feestwo.html')
