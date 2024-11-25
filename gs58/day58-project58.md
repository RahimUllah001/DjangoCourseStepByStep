
# Multi-Table Model Inheritance in Django

This project demonstrates how to implement **multi-table model inheritance** in Django.

## Models

In multi-table model inheritance, each model has its own database table. A parent model and its child models are connected through a one-to-one relationship.

We define two models: `ExamCenter` as the base model and `Student` as a child model.

### `models.py`

```python
from django.db import models

# Create your models here.
# Multi-table inheritance
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class Student(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
```

- `ExamCenter`: This model has fields `cname` (for the center name) and `city` (for the center's location).
- `Student`: This model inherits from `ExamCenter` and adds two additional fields: `name` (for the student's name) and `roll` (for the student's roll number).

Each `Student` entry will correspond to a unique `ExamCenter` entry, and Django automatically creates a one-to-one relationship between the two tables.

## Views

In the views, we retrieve the student data along with the exam center data.

### `views.py`

```python
from django.shortcuts import render
from .models import Student, ExamCenter

# Create your views here.

def home(request):
    student_data = Student.objects.all()
    exam_center = ExamCenter.objects.all()
    
    context = {'students': student_data, 'Examcenter': exam_center}
    return render(request, 'school/home.html', context)
```

- In this view, we fetch all `Student` and `ExamCenter` objects and pass them to the template using the context dictionary.

## Template

In the template, you can loop through the `students` and `Examcenter` to display their details.

### `home.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Student Data</h1>
    <ul>
        {% for student in students %}
        <li>{{ student.name }} - {{ student.roll }} - {{ student.cname }} - {{ student.city }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Conclusion

This implementation shows how to use multi-table inheritance in Django to manage relationships between models while ensuring that each model gets its own database table.
