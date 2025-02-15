"""
URL configuration for gs71 project.

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
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',views.myview, name='func'),
    # path('cl/',views.MyView.as_view(),name='cl')
    path('cl/',views.MyView.as_view(name="Muhammad"),name='cl'),
    path('ccl/',views.MyView.as_view(),name='ccl'),
    
    path('homefn/',views.RenderTemplatesByFuncView,name='hf'),
    path('homecl/',views.RenderTemplatesByClassView.as_view(),name = 'hcv'),

    # Rendering contact form
    path('formfn/',views.contactform,name='contact'),
    path('formcl/',views.ContactClassView.as_view(),name='CCv'),

    # rendering different templates from one view and passing them these templates name from url usinf function based view
    path('tf1/',views.DifferentTemplateByOneFuncView,{'templatename':"school/t1.html"},name="temp1"),
    path('tf2/',views.DifferentTemplateByOneFuncView,{'templatename':"school/t2.html"},name="temp2"),

    path('tc1/',views.DifferentTemplateByOneClassView.as_view(templatename="school/t1.html"),name="temp3"),
    path('tc2/',views.DifferentTemplateByOneClassView.as_view(templatename="school/t2.html"),name="temp3")

]
