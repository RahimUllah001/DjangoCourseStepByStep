# Day 3 Project-3:  Mapping Multiple URLs for the Same View

In this project, we explore the concept of mapping multiple URLs to the same view function. This technique can be useful for creating different URL patterns that all lead to the same functionality.

## Code Example

In the `urls.py` file, we define multiple URL patterns that point to the same view function:

```python
from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', views.learn_django),
    path('dj/', views.learn_django),  # Multiple URLs for the same view function
]

```

In this example, both `/learndj/` and `/dj/` are mapped to the `learn_django` view function. This demonstrates how you can use multiple URLs to access the same view.

## View Function

The `learn_django` view function is defined as follows:

```python
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse('learn django with us ')
    
```
This function returns a simple HTTP response with the text "learn django with us " when either of the defined URLs is accessed.