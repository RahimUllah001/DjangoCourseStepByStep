# GS12 - Static Files in Django

In this project, we demonstrate how to configure and use static files (CSS, JavaScript, images) in a Django project. We will cover setting up static files both within individual applications and in the root project folder.

## What are Static Files?

Static files include assets like CSS, JavaScript, and image files that don't change during the application's runtime. Django provides built-in support for handling static files.

**important message**
### If static files are located inside individual applications, Django automatically looks for them inside each app's 'static' folder. and their is no need for any configuration.

## Configuration Steps

### 1. Settings Configuration for Static Files

In the `settings.py` file, we need to make the following changes to handle static files located both inside the applications and in the root project folder.

```python
# Import necessary modules
from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Define STATIC_DIR for static files located in the root project folder
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # This is the URL path used to serve static files

# List of directories where Django will search for additional static files
STATICFILES_DIRS = [
    STATIC_DIR,  # Root-level static files
]

```
### Explanation of Settings Changes:
* STATIC_URL: This is the URL prefix used when referring to static files in HTML templates (/static/).
 STATICFILES_DIRS: A list where you define paths to static files that are outside the application directories, like in the root of the project.
* If you have static files inside your apps (like course/static/course/css/style.css), Django will automatically detect and include them as  - - long as django.contrib.staticfiles is added to INSTALLED_APPS (which is enabled by default).

## 2. Folder Structure for Static Files
We follow this folder structure in the project:

```
gs12/
│
├── static/                   # Root-level static files (for the whole project)
│   ├── css/
│   ├── js/
│   └── images/
│
├── course/
│   └── static/               # Static files for the 'course' app
│       ├── course/
│       │   ├── css/
│       │   ├── js/
│       │   └── images/
│
├── fees/
│   └── static/               # Static files for the 'fees' app
│       ├── fees/
│       │   ├── css/
│       │   ├── js/
│       │   └── images/

```
* **Root-Level Static Files**: We have a `static/` folder in the project root that holds static files for the entire project.
* **App-Level Static Files**: Each app (e.g., `course` and `fees`) has its own `static/` folder inside the app directory, containing app-specific CSS, JS, and image files.


## 3. Using Static Files in HTML Templates
In your HTML templates, you need to load the static tag using {% load static %} and reference static files using {% static 'path/to/file' %}.

Example:

```
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Including CSS from both root and app-level static folders -->
    <link rel="stylesheet" href="{% static 'css/some.css' %}">
    <link rel="stylesheet" href="{% static 'course/css/style.css' %}">
    <title>{{ title }}</title>
</head>
<body>
    <h2>{{ cname }}</h2>
    <!-- Including an image from app-level static files -->
    <img src="{% static 'course/images/a.jpeg' %}" alt="Image not available">
    
    <!-- Another way to include the static image -->
    <img src="{% get_static_prefix %}course/images/a.jpeg" alt="Image not available">
    
    <form action="">
        <input type="button" value="Click Me" onclick="disp()">
    </form>

    <!-- Including JavaScript from app-level static files -->
    <script src="{% static 'course/js/all.js' %}"></script>
    
    <!-- Another way to include JavaScript using get_static_prefix -->
    <script src="{% get_static_prefix %}course/js/all.js"></script>
</body>
</html>
```

## 4. Organizing Static Files in Apps
In the course and fees apps, we create individual static/course/ and static/fees/ directories where we place the CSS, JavaScript, and image files related to those apps. Django automatically serves these files when referenced in templates.

## 5. Testing and Serving Static Files
For development, Django will serve the static files automatically. However, in a production environment, you'll need to use a web server like Nginx or Apache to serve static files.