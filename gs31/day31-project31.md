# Project- Dynamic URL Configuration in Django

This project demonstrates how to set up dynamic URLs in Django for handling student details and sub-details using URL patterns with parameters. Below is a detailed breakdown of the URL configuration, views, and templates used in this project.

## Project Overview

The `gs31` project includes:
- Dynamic URL routing for displaying student details and sub-details.
- Custom views for handling different age categories.
- Templates for rendering student information based on dynamic URLs.

## URL Configuration

### Main `urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, {'check': 'ok'}, name='home'),
    path('student/', include('enroll.urls')),
]
```

### `enroll/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:my_id>/', views.show_details, name='detail'),
    path('<int:my_id>/<int:my_subid>/', views.show_subdetails, name='subdetail'),
]
```

## Views

### `home` View

The `home` view renders the home page and prints the `check` parameter.

```python
def home(request, check):
    print(check)
    return render(request, 'enroll/home.html')
```

### `show_details` View

The `show_details` view displays information about a student based on their ID. The student is categorized by age:

- If `my_id < 15`: Category is "bachay" (children)
- If `my_id > 15`: Category is "young"
- If `my_id > 50`: Category is "buzarg" (elderly)

```python
def show_details(request, my_id=1):
    if my_id < 15:
        student = {'id': my_id, "age_Category": "bachay"}
    elif my_id > 15 and my_id <= 50:
        student = {'id': my_id, 'age_Category': "young"}
    else:
        student = {'id': my_id, "age_Category": "buzarg"}

    return render(request, 'enroll/show.html', student)
```

### `show_subdetails` View

The `show_subdetails` view handles URLs with both `my_id` and `my_subid`. It categorizes students based on both parameters:

```python
def show_subdetails(request, my_id, my_subid):
    if my_id > 1 and my_subid < 15:
        student = {'id': my_id, "age_Category": "bachay", 'info': 'sub detail'}
    elif my_id > 15 and my_subid < 60:
        student = {'id': my_id, 'age_Category': "young", 'info': 'sub detail'}
    else:
        student = {'id': my_id, "age_Category": "buzarg", 'info': 'sub detail'}

    return render(request, 'enroll/show.html', student)
```

## Templates

### `enroll/home.html`

This is the home template where you can navigate to student details and sub-details:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <a href="{% url 'detail' 1 %}">Student 1</a>
    <a href="{% url 'detail' 2 %}">Student 2</a>
    <a href="{% url 'detail' 3 %}">Student 3</a>

    <a href="{% url 'subdetail' 2 10 %}">Sub Student 1</a>
    <a href="{% url 'subdetail' 20 50 %}">Sub Student 2</a>
    <a href="{% url 'subdetail' 61 100 %}">Sub Student 3</a>
</body>
</html>
```

### `enroll/show.html`

This template displays the student's details dynamically based on the URL parameters:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    This shows {{ id }} and the age category is {{ age_Category }} {{ info }}
    <a href="{% url 'home' %}">Back to home</a>
</body>
</html>
```

## Usage

- Navigate to `/student/<my_id>/` to view the details of a student with a specific ID.
- Navigate to `/student/<my_id>/<my_subid>/` to view sub-details for a specific student.
  
Example URLs:
- `http://127.0.0.1:8000/student/1/`
- `http://127.0.0.1:8000/student/4/1/`

## Conclusion

This project demonstrates the use of dynamic URLs in Django to handle complex views and URL patterns efficiently. It also shows how to pass variables from views to templates for dynamic content rendering.
