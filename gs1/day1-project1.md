# Django Crash Course Projects

This repository contains projects from my Django crash course. Each day, I create a new project and add something new to learn Django concepts.

## Day 1 - Project 1: Course Application

In the first project, I completed the following steps:

1. **Installed Python and Django**: I installed Django using `pip install django`.
2. **Created a Django Project**: Created Django projected using  'Django-admin startproject gs1' The project was named `gs1`.
3. **Created an Application**: Inside the project, I created an app called `course` using 'ython manage.py createapp course'.
4. **Added the App to `INSTALLED_APPS`**: I added the `course` app to the Django project's `settings.py`.
5. **Defined URLs**:
   - In the main `urls.py` file, I defined URL patterns and linked them to views from the `course` app:
     ```python
     # gs1/urls.py
     from django.contrib import admin
     from django.urls import path
     from course import views

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('learndj/', views.learn_django),
     ]
     ```
6. **Rendered HTML in Views**: I created a view in `views.py` to render an HTML template.

### Example Code
In `views.py`, the function looked like this:
```python
def learn_django(request):
    return HttpResponse('<h1> Hllo World!</h1>')

    <details>




    