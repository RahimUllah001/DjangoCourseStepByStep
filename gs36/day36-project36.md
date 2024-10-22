# User Registration with Django

In this project, we have implemented a user registration system using Django's built-in `UserCreationForm`. The system allows users to sign up with essential details like username, first name, last name, and email, and validates the input before saving the user information.

### Key Features:
- **Custom Sign-up Form**: We extend the `UserCreationForm` to customize the labels and include additional fields like `first_name`, `last_name`, and `email`.
- **Password Confirmation**: We add a confirmation field for the password (`password2`) for enhanced security.
- **Form Validation**: The form is validated upon submission, ensuring that all fields meet the required criteria before saving the user's details.
- **Success Message**: After successful registration, the system displays a message confirming the account creation.

### Code Overview:

#### Forms
```python
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class signUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
```

#### Registeration view function
```python
from django.shortcuts import render
from .forms import signUpForm
from django.contrib import messages

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