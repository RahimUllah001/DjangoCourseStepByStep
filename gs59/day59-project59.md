
# Proxy Model Inheritance in Django

This project demonstrates how to implement **proxy model inheritance** in Django.

## Models

Proxy model inheritance allows you to create a different behavior for an existing model without creating a new table in the database. In this example, `MyExamCenter` is a proxy model for `ExamCenter`.

### `models.py`

```python
from django.db import models

# Proxy inheritance: one table in the DB but different behavior for original and proxy models.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
```

- `ExamCenter`: This model has fields `cname` (for the center name) and `city` (for the center's location).
- `MyExamCenter`: This is a proxy model that shares the same database table as `ExamCenter`. However, it allows different behavior (e.g., custom admin behavior) without creating a new table in the database.

## Admin

In the Django admin, both models (`ExamCenter` and `MyExamCenter`) can be registered with different behavior.

### `admin.py`

```python
from django.contrib import admin
from .models import ExamCenter, MyExamCenter

# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']
    ordering = ['id']
```

- `ExamCenterAdmin`: The admin class for the `ExamCenter` model displays the fields `id`, `cname`, and `city`.
- `MyExamCenterAdmin`: The admin class for the `MyExamCenter` proxy model also displays the same fields but adds custom ordering by `id`.

This shows how the same table can be represented with different behavior in the admin interface.

## Conclusion

This implementation demonstrates the use of proxy model inheritance in Django, where a proxy model (`MyExamCenter`) is created to behave differently in the admin interface while sharing the same database table as the original model (`ExamCenter`).
