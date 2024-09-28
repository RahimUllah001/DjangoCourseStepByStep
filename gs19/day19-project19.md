# Project 19 - Day 19: Django Form Display Methods


In this project, I created a Django form using a form class, wrote a view to handle the form, and displayed the form in multiple ways within a template. Below is a step-by-step breakdown:

## 1. Django Form Creation
The form was created using Django’s `forms.Form` class. The fields included a `name`, `email`, and `first_name`:

```python
# forms.py
from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
```

## 2. View to Render the Form
I defined a view to render the form using Django's render method. This sends the form to the template for display.

```python
# views.py
from django.shortcuts import render
from .forms import StudentRegisteration

def showformdata(request):
    fm = StudentRegisteration()
    return render(request, 'enroll/userregisteration.html', {'form': fm})
```

## 3. Displaying the Form in the Template
The form is displayed in several different ways within the template:

### Basic Form Rendering
Displays the form with default styling.

```html
<form action="" method="get">
    {{ form }}
    <input type="submit" value="Submit">
</form>
```

### Displaying Form as a Table
Renders the form fields in a table-like format.

```html
<form action="" method="get">
    {{ form.as_table }}
    <input type="submit" value="Submit">
</form>
```

### Displaying Form as Paragraphs
Each form field is displayed as a paragraph.

```html
<form action="" method="get">
    {{ form.as_p }}
    <input type="submit" value="Submit">
</form>
```

### Displaying Form as an Unordered List
Each form field is rendered as a list item in an unordered list.

```html
<form action="" method="get">
    {{ form.as_ul }}
    <input type="submit" value="Submit">
</form>
```

### Displaying Specific Fields
This displays only specific form fields. For example, displaying only the name field:

```html
<form action="" method="get">
    {{ form.name }}
    <input type="submit" value="Submit">
</form>
```

Similarly, you can display only the email field:

```html
<form action="" method="get">
    {{ form.email }}
    <input type="submit" value="Submit">
</form>
```
