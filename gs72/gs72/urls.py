"""
URL configuration for gs72 project.

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
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
        # this url will show template file with out  writing view 
    path('',views.TemplateView.as_view(template_name='school/home.html'),name='home'), 
        # this url will show template file after writing view 
    path('uv',views.HomeTemplateView.as_view(),name='home'),

 
        # this url will show template file with writing view and passing context
    path('cc/<int:id>',views.ExtracContextTemplateView.as_view(extra_context = {"course":"python"}))
]
