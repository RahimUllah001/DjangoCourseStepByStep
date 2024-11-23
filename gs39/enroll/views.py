from django.shortcuts import render,HttpResponseRedirect
from .forms import signUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.models import User, Group
# Create your views here.

# Signup view function

def sign_up(request):
    if request.method == 'POST':
        fm = signUpForm(request.POST)

        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
            messages.success(request,'Account created successfully')
    else:
        fm = signUpForm()
    return render(request,'enroll/signup.html', {'form':fm})

# Login view Function

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username= uname, password = upass)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

# Dashboard
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')
# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
 























# Edit profile
def user_edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'profile updated!!!')
                fm.save()
                return HttpResponseRedirect('/profile/') 

        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'enroll/editprofile.html',{'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')
   