#   Django User Registration System using Model form

## Description

In this Django project, I demonstrated a user registration system using Django's Model Forms. Here's an overview of what I’ve accomplished:

### Model Definition

I defined a `User` model with `name`, `email`, and `password` fields. This model represents the user data in the database.

### Model Form Creation

I created a `StudentRegisteration` form that inherits from `forms.ModelForm`. This form automatically generates fields based on the `User` model and includes custom validation and widget options. I defined labels, error messages, and widgets for the form fields to customize the form’s appearance and behavior.

```python
from django import forms
from .models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Please enter your name',
            'email': 'Please enter your email',
            'password': 'Enter your password'
        }
        error_messages = {
            'name': {'required': 'Name field is required'}
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Write your name here'}),
        }
```

### Model Registration

I registered the `User` model with the Django admin interface to manage user data through the Django admin panel.

### View Implementation

I implemented the `showformdata` view to handle form submissions for user registration. This view processes POST requests to create or update user records based on the submitted data. I provided examples of how to create, update, and delete records using the Django ORM.


``` python
    from django.shortcuts import render
    from .forms import StudentRegisteration
    from .models import User

    def showformdata(request):      
        if request.method == 'POST':
            fm = StudentRegisteration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']
                # Insert data
                reg = User(name=nm, email=em, password=pw)
                reg.save()

                '''# Update specific data
                # reg = User(id=2, name=nm, email=em, password=pw)  # Update data 
                reg.save()
                '''

                '''# Delete data
                reg = User(id=2)
                reg.delete()
                '''
        else:
            fm = StudentRegisteration()
        return render(request, 'enroll/userregisteration.html', {'form': fm})




```



##  **Some extra work**


### Updating Records with Instance Method

- If you need to update an existing record, you can use the instance method to prepopulate the form with existing data:
   #### Code for updating record through instance method

    python
    '''
        def showformdata(request):      
            if request.method == 'POST':
                pi = User.objects.get(pk=1)
                fm = StudentRegisteration(request.POST, instance=pi)
                if fm.is_valid():
                    fm.save()
            else:
                fm = StudentRegisteration()
            return render(request, 'enroll/userregisteration.html', {'form': fm})
    ```

### Handling Updates and Creation Based on Fields Other Than ID
- To handle updates based on fields other than the primary key, you can use the following approach:
```
from django.shortcuts import render
from enroll.models import User
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print("post done")

            # Try to find the user by name
            try:
                # Check if a user with the given name exists
                reg = User.objects.get(name=nm)
                # If the user exists, update their details
                reg.email = em
                reg.password = pw
                print("Record found. Updating existing user.")
            except ObjectDoesNotExist:
                # If the user does not exist, create a new one
                reg = User(name=nm, email=em, password=pw)
                print("No matching record found. Creating a new user.")
            
            # Save the record (whether it's a new user or an update)
            reg.save()

    else:
        fm = StudentRegisteration()

    return render(request, 'enroll/userregisteration.html', {'form': fm})

```