"""
URL configuration for gs15 project.

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
from django.urls import path,include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    # path('about/',views.about), this is for simple url  making
    path('aboutme/',views.about,name = 'aboutus'),
    # path('cor/',include('course.urls')), #this is for simple url making
    path('corooo/',include('course.urls'))       # here i change the url but still working
]