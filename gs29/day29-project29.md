#   Django User Registration System using Form Api
## 1. Project Description
In Project 29, my  focus is  on how to creatw a Django form to accept user details, validate the input with custom error messages, and save the data to a database model. Additionally, i demonstrated  how to insert, update, and delete records in the database using Django's ORM.

## 2. Form Creation with Custom Error Messages:
- A form named StudentRegisteration was created with fields for name, email, and password. Custom error messages are provided for required fields.

## 3. Model Creation:
- A Django model User was created to store user data (name, email, and password).

## 4. Data Handling:
-The form data is validated and then inserted into the User model.
 Code snippets were included to demonstrate how to update and delete records using Django's ORM.

## Template:
- An HTML template (userregistration.html) was created to render the form and handle user input, with CSRF protection enabled.


## 5. Code
*   Form Creation
    The `StudentRegisteration` form is created with the following fields:
    - **Name** (CharField with custom error message)
    - **Email** (EmailField with custom error message)
    - **Password** (CharField with `PasswordInput` widget)

    ```python
        from django import forms

        class StudentRegisteration(forms.Form):
            name = forms.CharField(error_messages={'required':'Enter your name'}) 
            email = forms.EmailField(error_messages={'required':'Enter your email'})         
            password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your password'}) 
    ````    
        
*   **Model Creation**
        The User model is created to store user information (name, email, and password).

    ```python
        
        from django.db import models

        class User(models.Model):
            name = models.CharField(max_length=70)
            email = models.EmailField(max_length=70)
            password = models.CharField(max_length=70)
    ```
    *   **Form Handling in Views**
        In the view showformdata, the form is validated and the data is saved to the database using Django's ORM. The following operations are demonstrated:

        Insert: New data is inserted into the User model.
        Update: Code is included to update a specific record based on the ID.
        Delete: Code is included to delete a record based on the ID.

    ``` python
        from django.shortcuts import render
        from enroll.models import User
        from .forms import StudentRegisteration

        def showformdata(request):      
            if request.method == 'POST':
                fm = StudentRegisteration(request.POST)
                if fm.is_valid():
                    nm = fm.cleaned_data['name']
                    em = fm.cleaned_data['email']
                    pw = fm.cleaned_data['password']
                    
                    # Insert data into the database
                    reg = User(name=nm, email=em, password=pw)
                    reg.save()

                    '''
                    # Update existing record
                    reg = User(id=3, name=nm, email=em, password=pw)
                    reg.save()
                    '''

                    '''
                    # Delete a record
                    reg = User(id=10)
                    reg.delete()
                    '''
            else:
                fm = StudentRegisteration()
            return render(request, 'enroll/userregisteration.html', {'form': fm})

    ```