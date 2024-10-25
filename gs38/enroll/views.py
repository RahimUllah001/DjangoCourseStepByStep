from django.shortcuts import render,HttpResponseRedirect
from .forms import signUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

# Signup view function

def sign_up(request):
    if request.method == 'POST':
        fm = signUpForm(request.POST)

        if fm.is_valid():
            fm.save()
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
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# profile
def user_profile(request):
    if request.user.is_authenticated:

        if request.user.is_superuser == True:
            fm = EditAdminProfileForm(instance=request.user)
            users = User.objects.all()
        else:
            fm = EditUserProfileForm(instance=request.user)
            users = None
        
        # Disable all fields
        for field in fm.fields.values():
            field.disabled = True
        
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm,'users':users })
    else:
        return HttpResponseRedirect('/login/')




# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



# Change Password with old Password
def user_change_pass(request):
    print(f"User authenticated: {request.user.is_authenticated}")  
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                # update_session_auth_hash(request,fm.user)   #by writing this line the seesion will notb e expire and we redirect to prfile instead of login
                messages.success(request,'Password change successfully')
                return HttpResponseRedirect('/profile/')        # here we have written redirect to profile but it redirect us to login because after changing password our session expires so thats why we are not authenticated and it reidrect us to login ==> session expires
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/') 
    


# Change Password without old Password
def user_change_pass1(request):
    print(f"User authenticated: {request.user.is_authenticated}")  
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                # update_session_auth_hash(request,fm.user)   #by writing this line the seesion will notb e expire and we redirect to prfile instead of login
                messages.success(request,'Password change successfully')    #this messge will be shown if i uncomment he above line mean when the session not get expires
                return HttpResponseRedirect('/profile/')        # here we have written redirect to profile but it redirect us to login because after changing password our session expires so thats why we are not authenticated and it reidrect us to login ==> session expires
        else:
            fm = SetPasswordForm(user = request.user)
        return render(request,'enroll/changepass1.html', {'form':fm})
    else:
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
    

def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')