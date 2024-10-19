# Project: Django Multi-App Architecture: Exploring Dual URL Mapping Techniques
*This project demonstrates two approaches to URL mapping in Django*

In the first project, I completed the following steps:

## 2. **Created a Django Project**: Created Django projected using  'Django-admin startproject gs1' The project was named `gs1`.
## 3. **Created an Application**: Inside the project, I created two apps called `course` using 'python manage.py createapp course' and `fees`    using 'python manage.py createapp fees'.

## 4. **Added the App to `INSTALLED_APPS`**: I added the `course` and `fees` apps  to the Django project's `settings.py`.

## 5. **Defined URLs:**

In this project, there are two ways to map URLs to their respective views:

* 1. **Using Aliases for View Imports**:
    - We can create aliases for the views in the different applications to ensure there are no naming conflicts and to make the code more readable.
    - Example of defining aliases:
    ```python
    from course import views as cv
    from fees import views as fv
    ```
    Then the URL configuration would look like:
    ```python
    path('learndj/', cv.learn_django),
    path('feesdj/', fv.fees_django),
    ```

* 2. **Direct View Imports**:
    - Alternatively, we can import the view functions directly from each app and map them to URLs. This is a more straightforward approach when there are fewer views or no name conflicts.
    - Example of direct imports:
    ```python
    from course.views import learn_django
    from fees.views import fees_django
    ```

    **Final URL Configuration:**
    The following code maps the URLs to their respective views using direct imports:
    ```python
    from django.contrib import admin
    from django.urls import path
    from course.views import learn_django     # Importing directly from course app
    from fees.views import fees_django        # Importing directly from fees app

    urlpatterns = [
        path('admin/', admin.site.urls),      # Admin route
        path('learndj/', learn_django),       # Maps to learn_django view in course app
        path('feesdj/', fees_django),         # Maps to fees_django view in fees app
    ]
    ```

---

## 6. **Explanation of URL Mapping**:
- **`path('learndj/', learn_django)`**: This maps the `/learndj/` URL to the `learn_django` view function in the `course` app. When a user visits this URL, the `learn_django` view will handle the request and return the appropriate response.
- **`path('feesdj/', fees_django)`**: This maps the `/feesdj/` URL to the `fees_django` view in the `fees` app, handling fee-related logic.

---

## 7. **Advantages**:
- **Alias Method**: Useful when we have multiple views with the same name across different apps, avoiding name clashes.
- **Direct Import Method**: Cleaner and more direct, recommended for small projects or when view names are unique across the project.

---

## 8. **Summary**:
This project demonstrates two approaches to URL mapping in Django. Both methods are flexible and depend on the complexity of the project. For simplicity, direct view imports are used in this project, but aliasing can be introduced in larger, more complex applications.
