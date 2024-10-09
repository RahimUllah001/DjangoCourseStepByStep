# Project - User Registration with Password Matching in Django

This project demonstrates how to create a user registration form in Django using `forms.Form` and implement password matching validation. Below is a detailed breakdown of the form setup, views, and templates used in this project.

## Project Overview

The `gs28` project includes:
- A custom form `StudentRegisteration` with fields for name, email, password, and repeated password.
- Validation logic to ensure that the password and repeated password fields match.
- A view to handle form submission and rendering.
- A template for displaying the form and handling CSRF protection.

## Forms

### `StudentRegisteration` Form

The form includes fields for `name`, `email`, `password`, and `rpassword` (repeat password). It also has a custom validation method `clean` to ensure password matching.

```python
from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField()         
    password = forms.CharField(widget=forms.PasswordInput)        
    rpassword = forms.CharField(label='Password(again)', widget=forms.PasswordInput)

    def clean(self):
        clean_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']

        if valpwd != valrpwd:
            raise forms.ValidationError("Passwords do not match")
```



##  Views
    showformdata View
    The view handles form submission and validation. If the form is valid, a success message is printed to the console. If not, the form is re-rendered with error messages.
```
    python
    from django.shortcuts import render
    from .forms import StudentRegisteration
    from django.http import HttpResponseRedirect

    def showformdata(request):
        if request.method == 'POST':
            fm = StudentRegisteration(request.POST)
            if fm.is_valid():
                print("Form validated")
        else:
            fm = StudentRegisteration()
        return render(request, 'enroll/userregisteration.html', {'form': fm})
```
##  Template
    userregisteration.html
    This is the HTML template that renders the form and handles the form submission via POST method. It includes CSRF protection.

    html
``` <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Registration</title>
    </head>
    <body>
        <form action="" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
```    
##  Features
   * Password Matching: The form includes custom validation to ensure that the password and the repeated password match. If they do not, a validation error is raised.
    Form Handling: The form is submitted via POST, and the view handles both form validation and error messages.
    CSRF Protection: The form template includes CSRF tokens for security during form submission.

