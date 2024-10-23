from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.

def setcookie(request):
    response = render(request, 'student/setcookie.html')
    # response.set_cookie('name', 'rahim',max_age=120)#WE CAN USE THIS WAY ALSO THE BLOW LINE MAXAGE MEAN SHOW MUCH TIME FOR EXPIRY
    response.set_cookie('name', 'rahim',expires=datetime.utcnow()+timedelta(days=1))        #set expiry date for cookie
    return response

def getcookie(request):
    # name = request.COOKIES['name']        # one way to get cookie
    name = request.COOKIES.get('name',"Guest")       # 2nd way to get cookie but thriugh thid eay it give none when cookie not present and not give any rror alos we can set default vlaue for cookie as here like guest
    return render(request,'student/getcookie.html',{'name':name})


def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name', 'rahim')
    return response


# how to use signed cookies below both function for this purpose
def setsaltcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'NASIR',salt= 'nm' ,expires=datetime.utcnow()+timedelta(days=1))        #set expiry date for cookie
    return response


def getcookie(request):
    name = request.get_signed_cookie('name',salt='nm')  
    return render(request,'student/getcookie.html',{'name':name})

# delete is same for above and below