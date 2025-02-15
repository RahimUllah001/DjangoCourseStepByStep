
# Project 71 - Django Class-Based Views (CBVs)

In this project, I demonstrated how to implement Django class-based views (CBVs) for rendering content, handling forms, and switching between different templates using the same view. The project also compares CBVs with function-based views (FBVs) for a clearer understanding.

## Code and Explanation

### 1. Returning HTML Content

#### Function-Based View (FBV)
```python
# views.py
from django.http import HttpResponse

def myview(request):
    return HttpResponse('<h1>Function based view</h1>')
```
- This FBV returns a simple HTML response when the URL is accessed.

#### Class-Based View (CBV)
```python
from django.views import View

class MyView(View):
    name = "rahim"

    def get(self, request):
        return HttpResponse(self.name)
```
- A CBV is defined by inheriting from `View`.
- The `get` method handles GET requests and returns a response containing a class attribute `name`.

### 2. Child Class Example

```python
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
```
- This child class inherits from `MyView` and overrides the `get` method.

### 3. Rendering Templates

#### Function-Based View
```python
from django.shortcuts import render

def RenderTemplatesByFuncView(request):
    return render(request, 'school/home.html', {"method": "Function_based"})
```
- This FBV renders a template and passes a context variable to display the method type.

#### Class-Based View
```python
class RenderTemplatesByClassView(View):
    def get(self, request):
        return render(request, 'school/home.html', {"method": "class_based"})
```
- The CBV renders the same template but uses the `get` method to handle the request.

### 4. Handling Forms

#### Function-Based View
```python
from .forms import ContactForm

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you, your form was submitted by function based view method')
    else:
        form = ContactForm()  # Empty form for GET request

    return render(request, 'school/contact.html', {'form': form})
```
- This FBV handles form submission by checking the request method and validating the form.

#### Class-Based View
```python
class ContactClassView(View):
    def get(self, request):
        form = ContactForm()  # Empty form for GET request
        return render(request, 'school/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you, your form was submitted by Class based view method.')
```
- The CBV uses separate `get` and `post` methods to handle form rendering and submission respectively.

### 5. Rendering Different Templates Using One View

#### Function-Based View
```python
def DifferentTemplateByOneFuncView(request, templatename):
    context = {"name": "Rahim"}
    return render(request, templatename, context)
```
- This FBV dynamically renders different templates based on the template name passed in the URL.

#### Class-Based View
```python
class DifferentTemplateByOneClassView(View):
    templatename = ""

    def get(self, request):
        context = {"name": "Rahim"}
        return render(request, self.templatename, context)
```
- The CBV uses a class attribute `templatename` and renders the appropriate template.

## URLs Configuration

```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.myview, name='func'),
    path('cl/', views.MyView.as_view(name="Muhammad"), name='cl'),
    path('ccl/', views.MyView.as_view(), name='ccl'),
    path('homefn/', views.RenderTemplatesByFuncView, name='hf'),
    path('homecl/', views.RenderTemplatesByClassView.as_view(), name='hcv'),
    path('formfn/', views.contactform, name='contact'),
    path('formcl/', views.ContactClassView.as_view(), name='CCv'),
    path('tf1/', views.DifferentTemplateByOneFuncView, {'templatename': "school/t1.html"}, name="temp1"),
    path('tf2/', views.DifferentTemplateByOneFuncView, {'templatename': "school/t2.html"}, name="temp2"),
    path('tc1/', views.DifferentTemplateByOneClassView.as_view(templatename="school/t1.html"), name="temp3"),
    path('tc2/', views.DifferentTemplateByOneClassView.as_view(templatename="school/t2.html"), name="temp4")
]
```
- The `urlpatterns` list defines the routes for both function-based and class-based views.
- Different templates can be rendered by passing their names via the URL.

## Form Definition

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
```
- A simple form with a single `name` field of type `CharField`.

## Summary

This project illustrates how to implement class-based views for various functionalities in Django, including rendering templates, handling forms, and dynamically switching templates. By comparing them with function-based views, learners can better understand when and how to use CBVs effectively.