"""
URL configuration for gs5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from course import views as cv
from course.views import learn_django     #instead above line we can also do through this line the same
# from fees import views as fv
from fees.views import fees_django      #instead above line we can also do through this line the same



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('learndj/',cv.learn_django),
    path('learndj/',learn_django),      #instead above line we can also do through this line the same

    # path('feesdj/',fv.fees_django),
    path('feesdj/',fees_django),         #instead above line we can also do through this line the same


]
