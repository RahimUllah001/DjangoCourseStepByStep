from django.shortcuts import render

# Create your views here.

def check_templates_inside_application(request):
    return render(request, 'fees/info.html')