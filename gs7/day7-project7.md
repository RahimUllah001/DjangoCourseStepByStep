# Project gs7: Direct URL Definition and Inclusion Method

## Project Overview

In this project, URL patterns for different views are managed directly in the main `urls.py` file without creating separate app-level `urls.py` files. This approach involves defining URL patterns directly in the main project's `urls.py` and including them using the `include()` function.

## URL Configuration

### 1. **Direct URL Definitions**

```python
from django.contrib import admin
from django.urls import path, include
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include([
        path('learndj/', cv.learn_django),
        path('learnpy/', cv.learn_python)
    ])),
    path('fee/', include([
        path('feedj/', fv.fee_django),
        path('feepy/', fv.fee_python)
    ]))
]

```

### 2. **Using Pattern Lists**
```
from django.contrib import admin
from django.urls import path, include
from course import views as cv
from fees import views as fv

coursepatterns = [
    path('learndj/', cv.learn_django),
    path('learnpy/', cv.learn_python)
]

feepatterns = [
    path('feedj/', fv.fee_django),
    path('feepy/', fv.fee_python)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include(coursepatterns)),
    path('fee/', include(feepatterns))
]

```
### 2. **Explanation**
- Summary
This project demonstrates two ways of configuring URLs directly within the main urls.py file. The first method defines URL patterns inline, while the second method organizes them into separate lists before including them. Both approaches achieve the same result but may differ in readability and organization.