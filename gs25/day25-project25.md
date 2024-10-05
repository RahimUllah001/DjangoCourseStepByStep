# Project: Django Form Submission and Success Message

## Overview
In this project, we implemented a form for student registration using Django forms. Upon successful submission of the form via the `POST` method, the user is redirected to a success page. The form data is processed, validated, and cleaned before it is used.

### HTTP Methods Used:
- **GET**: When the form is initially loaded, a `GET` request is used to display the empty form to the user.
- **POST**: When the user submits the form, a `POST` request is made. The form data is then validated, cleaned, and processed.

### HTTP Response Handling:
- **HttpResponseRedirect**: After the form is successfully submitted, the user is redirected to a success page using `HttpResponseRedirect` to avoid resubmission on page reload.

## Key Concepts Covered:
- Handling `POST` and `GET` requests in Django
- Form validation in Django
- Redirecting after form submission using `HttpResponseRedirect`
- Accessing form data using `cleaned_data`

---

## Code Implementation

### `views.py`

```python
from django.shortcuts import render
from .forms import StudentRegisteration
from django.http import HttpResponseRedirect

# View for success page after form submission
def on_submission(request):
    return render(request, 'enroll/success.html')

# View to handle form data
def showformdata(request):
    if request.method == 'POST':
        # When form is submitted via POST request
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            # If form is valid, clean and retrieve data
            print("Data received through POST method:")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            
            # Redirect to success page after form submission
            return HttpResponseRedirect('/regi/formsubmitted')
    else:
        # If GET request, show empty form
        fm = StudentRegisteration()
        print("GET method is active now.")
        
    return render(request, 'enroll/userregisteration.html', {'form': fm})
```



## POST Method
When the form is submitted using the `POST` method, it captures the data sent by the user. The form is validated, and if all fields are correct, the data is cleaned using `cleaned_data`. After validation, the user is redirected to the success page using `HttpResponseRedirect`.

### Detailed Explanation of the Workflow

**User Accesses Form**:  
When a user accesses the form URL, a `GET` request is sent to the server. The `showformdata` view function handles this request, rendering the `userregisteration.html` form.

**User Submits Form**:  
When the user fills out the form and clicks the submit button, a `POST` request is sent to the server with the form data. The view function processes this data by checking if the form is valid.

**Form Validation**:  
The data is cleaned and validated using Django's built-in form validation methods. If everything is correct, the form is considered valid.

**Data Handling**:  
The cleaned data is extracted using the `cleaned_data` attribute of the form. The user’s name, email, and password are retrieved.

**Redirect After Submission**:  
After successful form submission, the user is redirected to the success page using `HttpResponseRedirect`, which prevents the form from being re-submitted if the page is refreshed.

**Success Page**:  
The success page (`success.html`) is rendered with a personalized message for the user.
