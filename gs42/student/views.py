from django.shortcuts import render,HttpResponse

# Create your views here.

def setsession(request):
    request.session['name'] = 'Rahim'
    return render(request,'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        
        name = request.session['name']
        request.session.modified = True
        return render(request,'student/getsession.html',{'name':name})
    else:
        return HttpResponse("Your Session has been Expired...")
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')