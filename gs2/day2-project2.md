# Project 2, Day 2 - Django HTTP Responses

In this project, we created a Django project named **gs2** and an application named **course**. We implemented various views inside the **course** app that return different types of HTTP responses.

## Project Setup

1. **Create a Django project:**
   - Command: `django-admin startproject gs2`

2. **Create an application inside the project:**
   - Command: `python manage.py startapp course`

3. **Register the application in `settings.py`:**
   In the `INSTALLED_APPS` section of **gs2/settings.py**, add the application **course**:
   - `'course'` to the list of installed apps.

## Views Implementation

In the **views.py** file of the **course** application, we defined several views that return different types of HTTP responses:

### 1. Simple Text Response
This view returns a simple string as an HTTP response:
   - `index(request)` returns `'Home Page'`.

### 2. Custom Text Response
This view returns a custom string response:
   - `learn_django(request)` returns `'Hello Django'`.

### 3. HTML Response
This view returns an HTML formatted response:
   - `learn_python(request)` returns `<h1>Hello Python<h1/>`.

### 4. Using Variables in Response
In this view, we used a variable to store an HTML string and returned it:
   - `learn_var(request)` stores HTML in a variable `a` and returns it.

### 5. Mathematical Calculation in Response
This view performs a simple mathematical operation (addition) and returns the result:
   - `learn_math(request)` returns the sum of `10 + 10`, which is `20`.

### 6. String Formatting in Response
In this view, we used Python string formatting (f-string) to dynamically insert a value into the response:
   - `learn_format(request)` returns `'Hello How are u Geeky shows'`.

## URL Configuration

Finally, configure the URLs in the **urls.py** file of the **gs2** project to map the views:
   - `/` → `index()`
   - `/learn_django/` → `learn_django()`
   - `/learn_python/` → `learn_python()`
   - `/learn_var/` → `learn_var()`
   - `/learn_math/` → `learn_math()`
   - `/learn_format/` → `learn_format()`

## Running the Project

To run the project, use the command: `python manage.py runserver`.

Visit the following URLs in your browser to test the HTTP responses:
   - `http://127.0.0.1:8000/` → Home Page
   - `http://127.0.0.1:8000/learn_django/` → Hello Django
   - `http://127.0.0.1:8000/learn_python/` → Hello Python (in HTML format)
   - `http://127.0.0.1:8000/learn_var/` → Hello Python (using variable)
   - `http://127.0.0.1:8000/learn_math/` → 20 (result of 10 + 10)
   - `http://127.0.0.1:8000/learn_format/` → Hello How are u Geeky shows
