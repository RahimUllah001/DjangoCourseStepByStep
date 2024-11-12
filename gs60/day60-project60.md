
# Managers and Custom Managers in Django

In Django, **Managers** are used to interact with the database. A manager is an interface through which model queries are made. By default, Django provides a default manager called `objects`. However, you can also define your own custom manager to modify or extend the default query behavior.

## Default Manager

The default manager provided by Django is named `objects`. If you don’t specify any custom manager, Django automatically adds it for you.

### Example: Default Manager

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

# Default manager is automatically available as 'objects'
```

In this example, the `Student` model has a default manager called `objects`. You can use this manager to retrieve data from the database.

```python
student_data = Student.objects.all()  # Fetches all students
```

## Custom Managers

You can create a **custom manager** by subclassing `models.Manager` and adding custom methods to the manager class. Custom managers are useful when you want to encapsulate specific query logic.

### Example: Custom Manager

```python
from django.db import models

class CustomManager(models.Manager):
    # Custom method for filtering based on roll number range
    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))
```

In this example, `CustomManager` defines a custom method `get_stu_roll_range()` that retrieves students whose roll numbers fall within a given range.

### Applying the Custom Manager

To use the custom manager, you need to add it to the model.

```python
from django.db import models
from .managers import CustomManager

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # Add default manager
    objects = models.Manager()
    
    # Add custom manager
    students = CustomManager()
```

- `objects`: This is the default manager that will still be available.
- `students`: This is the custom manager that allows you to use the custom method defined in `CustomManager`.

## Using the Custom Manager

With the custom manager in place, you can call the custom method to filter students by roll number range.

```python
# Using the custom manager to get students within a roll range
student_data = Student.students.get_stu_roll_range(112, 114)
```

### Views

Here’s how you can use the custom manager inside a Django view.

```python
from django.shortcuts import render
from .models import Student

def home(request):
    student_data = Student.students.get_stu_roll_range(112, 114)  # Custom manager method
    return render(request, 'school/home.html', {'students': student_data})
```

## Conclusion

Managers are the gateway to interacting with your Django models. By default, Django provides the `objects` manager, but you can define custom managers to add specific query methods that suit your business logic. Custom managers are powerful tools for writing clean, reusable code in your Django applications.
