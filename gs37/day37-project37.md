# User Authentication and Profile Management in Django

This project demonstrates user authentication, profile management, and password management functionalities in a Django application. The application includes views for user signup, login, profile display, password change (with and without old password), and profile editing. 

## Project Structure

The project contains the following main components:

- `urls.py`: URL routing for the application.
- `views.py`: Logic for handling user requests.
- `forms.py`: Form definitions for user authentication and profile editing.
- Templates: HTML files for rendering user interfaces.

## URL Configuration (`urls.py`)

The `urls.py` file defines the routes for the application. The following routes are implemented:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('change_pass/', views.user_change_pass, name='changepass'),
    path('change_pass1/', views.user_change_pass1, name='changepass1'),
    path('edit_profile/', views.user_edit_profile, name='edit_profile'),
]
```

## View Functions (`views.py`)

### 1. Signup View

Handles user registration. It uses a custom form (`signUpForm`) to create a new user.

```python
def sign_up(request):
    if request.method == 'POST':
        fm = signUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfully')
    else:
        fm = signUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})
```

### 2. Login View

Manages user login using Django's `AuthenticationForm`. If the user is already logged in, it redirects to the profile.

```python
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')
```

### 3. User Profile View

Displays user profile and allows editing of profile details.

```python
def user_profile(request):
    if request.user.is_authenticated:
        fm = EditUserProfileForm(instance=request.user)
        
        # Disable all fields
        for field in fm.fields.values():
            field.disabled = True
        
        return render(request, 'enroll/profile.html', {'name': request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/login/')
```

### 4. Logout View

Logs out the user and redirects to the login page.

```python
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
```

### 5. Change Password Views

Includes two views for changing the user password:

- **With old password**:

```python
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
```

- **Without old password**:

```python
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
```

### 6. Edit Profile View

Allows the user to edit their profile information.

```python
def user_edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile updated!')
                fm.save()
                return HttpResponseRedirect('/profile/')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/editprofile.html', {'name': request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/login/')
```

## Forms (`forms.py`)

### 1. Signup Form

Custom form for user registration.

```python
class signUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
```

### 2. Edit User Profile Form

Form for editing user details.

```python
class EditUserProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}
```

## Templates

### 1. Signup Template (`signup.html`)

```html
<form action="" method="post" novalidate>
    {% csrf_token %}
    {% for fm in form %}
        {% if fm.name != 'usable_password' %}
            {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }} <br><br>
        {% endif %}
    {% endfor %}
    <input type="submit" value="Submit">
</form>
```

### 2. Login Template (`login.html`)

```html
<form action="" method="post" novalidate>
    {% csrf_token %}
    {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
    {% endfor %}
    <input type="submit" value="Login">
</form>
```

### 3. Profile Template (`profile.html`)

```html
<h2>Welcome, {{ name | capfirst }}</h2>
<form method="post">
    {% csrf_token %}
    {% for fm in form %}
        {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }} <br><br>
    {% endfor %}
</form>
<p>
    <button><a href="{% url 'changepass1' %}">Change Password without old</a></button>
    <button><a href="{% url 'changepass' %}">Change Password</a></button>
    <button><a href="{% url 'logout' %}">Logout</a></button>
    <button><a href="{% url 'edit_profile' %}">Edit Profile</a></button>
</p>
```

### 4. Edit Profile Template (`editprofile.html`)

```html
<form action="" method="post" novalidate>
    {% csrf_token %}
    {% for fm in form %}
        {{fm.label_tag}} {{fm}} {{fm.errors|striptags}} <br><br>
    {% endfor %}
    <input type="submit" value="Save">
</form>
```

## Conclusion

This Django application provides a comprehensive solution for user management, including registration, login, profile editing, and password management. The implementation of form handling, user authentication, and templating demonstrates the core capabilities of Django in building secure web applications.

