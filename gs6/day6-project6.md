# Day 6 - Project 6: Efficient URL Configuration in Django"
- This project demonstrates how to structure URLs in a Django project by using individual urls.py files within each app and including them in the main project’s urls.py. This modular approach helps in managing URLs more efficiently and keeps the project organized, making it easier to scale and maintain.---

In the first project, I completed the following steps:

## 2. **Created a Django Project**: Created Django projected using  'Django-admin startproject gs1' The project was named `gs1`.
## 3. **Created an Application**: Inside the project, I created two apps called `course` using 'python manage.py createapp course' and `fees`    using 'python manage.py createapp fees'.

## 4. **Added the App to `INSTALLED_APPS`**: I added the `course` and `fees` apps  to the Django project's `settings.py`.

## 5. **Defined URLs:**

I make url.py file inside each application:

    * url for fees application
```
    from django.urls import path

    from . import views

    urlpatterns = [
        path('feedj/',views.fee_django),
        path('feepy/',views.fee_python),
    ]
```

    * url.py for course application
    ```
    from django.urls import path

    from . import views

    urlpatterns = [
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
    ]
    ```


## 6. Configure URLs in the Main Project
    ```from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('cor/',include('course.urls')),
        path('fee/',include('fees.urls')),
    ]
    ```
---

### 7. Advantages

- Modular URL Management: By creating separate `urls.py` files for each app, the URL configuration is more modular and easier to manage, especially in larger projects.
- Scalability: This approach scales better as the project grows. Each app's URL routing is handled independently, making it easier to add or modify routes without affecting the main project configuration.
- Cleaner Code: Keeps the main `urls.py` file cleaner and more organized by delegating routing responsibilities to the respective app’s `urls.py`.
