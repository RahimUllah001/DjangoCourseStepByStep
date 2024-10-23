from django.shortcuts import render,HttpResponseRedirect
from .forms import signUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.urls import reverse
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
        fm = EditUserProfileForm(instance=request.user)
        
        # Disable all fields
        for field in fm.fields.values():
            field.disabled = True
        
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm})
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
    


    # //////////////////////////////////////////
    url.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name= 'signup'),
    path('login/', views.user_login,name='login'),
    path('profile/', views.user_profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
    path('change_pass/', views.user_change_pass,name='changepass'),
    path('change_pass1/', views.user_change_pass1,name='changepass1'),
    path('edit_profile/', views.user_edit_profile,name='edit_profile'),

views.py

from django.shortcuts import render,HttpResponseRedirect
from .forms import signUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.urls import reverse
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
        fm = EditUserProfileForm(instance=request.user)
        
        # Disable all fields
        for field in fm.fields.values():
            field.disabled = True
        
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm})
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

form.py
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class signUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {'email': 'Email'}

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','date_joined', 'last_login']
        labels = {'email' : 'Email'}


signup.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
<form action="" method="post" novalidate>
    {% csrf_token %}
    {% for fm in form %}
        {% if fm.name != 'usable_password' %}  <!-- Exclude the usable_password field -->
            {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }} <br><br>
        {% endif %}
    {% endfor %}
    <input type="submit" value="Submit">
</form>
<!-- Displaying success and other messages -->
{% if messages %}
        {% for message in messages %}
            {{ message }} 
        {% endfor %}
{% endif %}

<a href="{% url "login" %}">Log In</a>

</body>
</html> 

{% comment %} if i want not show enable and disable button {% endcomment %}
{% comment %} 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registeration</title>
</head>
<body>
<form action="" method="post" novalidate>
    {% csrf_token %}
    {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
    {% endfor %}

<input type="submit" value="Submit">

</form>

{% if messages %}
{% for message in messages  %}

{{message}}
{% endfor %}
{% endif %}
</body>
</html> {% endcomment %} 

login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
</head>
<body>
    <form action="" method="post" novalidate>
        {% csrf_token %}

        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p style = "color : red ">{{error}}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
         {% endfor %}        
    <input type="submit" value="Login">
    </form>
    <a href="{% url "signup" %}">Sign Up</a>
</body>
</html>

profile.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
    <h2>Welcome, {{ name | capfirst}}</h2>

    <form method="post">
        {% csrf_token %}

        {% for fm in form %}
            {{ fm.label_tag }}
            {{ fm }}
            {{ fm.errors|striptags }}
            <br><br>
        {% endfor %}
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}

    <p>
        <button><a href="{% url 'changepass1' %}">Change Password without old</a></button>
        <button><a href="{% url 'changepass' %}">Change Password</a></button>
        <button><a href="{% url 'logout' %}">Logout</a></button>
        <button><a href="{% url 'edit_profile' %}">Edit Profile</a></button>
    </p>
</body>
</html>
editprofile.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile edition</title>
</head>
<body>
    Wellcome Dear {{name}}

    <form action="" method="post" novalidate>
        {% csrf_token %}

        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p style = "color : red ">{{error}}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
         {% endfor %}        
    <input type="submit" value="Save">
    </form>
</body>
</html>  
{% comment %} 

# profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'profile uploadded!!!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/') {% endcomment %}

changepass.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
</head>
<body>
    <form action="" method="post" novalidate>
        {% csrf_token %}

        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p style = "color : red ">{{error}}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
         {% endfor %}        
    <input type="submit" value="Save">
    <a href="{% url "profile" %}">Profile</a>
    <a href="{% url "logout" %}">Logout</a>
    </form>
</body>
</html>

changepass1.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
</head>
<body>
    <form action="" method="post" novalidate>
        {% csrf_token %}

        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p style = "color : red ">{{error}}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
         {% endfor %}        
    <input type="submit" value="Save">
    <a href="{% url "profile" %}">Profile</a>
    <a href="{% url "logout" %}">Logout</a>
    </form>
</body>
</html>

in this project I  have achieved this work which is is shown in urls.py how I achieve this it is also here all the files related to this i.e form and views and respected templates plz write a detail md file for this and provide me the link so that I can download it thanks in advance 