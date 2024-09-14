# Project gs9: How to use templates in django 

## 1. Description of the
In this project, I demonstrated how to integrate and use Django templates to dynamically generate HTML content. I set up a Django project with two applications, course and fees, and configured the settings.py to locate template directories. The project involved creating various HTML templates and rendering them from a view function, showcasing different ways to pass context data to templates.



In the first project, I completed the following steps:

## 2. **Created a Django Project**: Created Django projected using  'Django-admin startproject gs9' The project was named `gs9`.
## 3. **Created an Application**: Inside the project, I created two apps called `course` using 'python manage.py createapp course' and `fees`    using 'python manage.py createapp fees'.

## 4. **Added the App to `INSTALLED_APPS`**: I added the `course` and `fees` apps  to the Django project's `settings.py`
    -Installed apps
    INSTALLED_APPS = [
        'course',
        'fees',
        # other apps...
    ]


## 5. Creating templates Folder
-   created a templates folder inside root directory of prject

## 6. Folder structure

    gs9
    ├── templates
    │   ├── courseone.html
    │   ├── coursetwo.html
    │   ├── feesone.html
    │   ├── feestwo.html
    ├── gs9
    ├── manage.py
    └── course
    └── fees

## 7. Required Modifications in settings.py
-Add the following settings in settings.py to configure the template directories:
import os

### Define the directory for templates
 TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

### TEMPLATES configuration
TEMPLATES = [
    {
        'DIRS': [TEMPLATES_DIR],  # Directories where the engine should look for template source files
    },
]

## 8. how to contact templates from view function 
```
def learn_django(request):
    coursename = {'cname': 'Django'}
        return render(request, 'course/courseone.html', context=coursename)


    # 1st Way
    return render(request, 'course/courseone.html', context=coursename)

    # 2nd Way
    return render(request, 'course/courseone.html', coursename)

    # 3rd Way
    return render(request, 'course/courseone.html', {'cname': 'Django'})
```




## 9. Template
    A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

    A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

    Template is used by the view function to represent the data to the user.

    The user sends a request to view, then view contacts the template, afterward the view gets information from the template and then the view gives a response to the users.
