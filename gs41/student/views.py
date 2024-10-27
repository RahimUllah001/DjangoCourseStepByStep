from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def setsession(request):
    request.session['name'] = 'Rahim'
    return render(request,'student/setsession.html')


def getsession(request):
    # name = request.session['name']        or the below one
    name = request.session.get('name')
    return render(request,'student/getsession.html', {'name':name})


def delsession(request):
    request.session.flush()     #this also not clear the db fully
    request.session.clear_expired()     #this will clear db 
    
    # if 'name' in request.session:
        # del request.session['name']       this line not toatlly delte the sesion but the key remain
    return render(request,'student/delsession.html')