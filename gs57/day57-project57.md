
# Django Model Inheritance: Abstract Base Class

In this project, I have implemented **model inheritance** in Django using **abstract base classes**. Below is an explanation of the project:

## What is Model Inheritance?

Django provides a way to reuse fields and logic across multiple models using **model inheritance**. One such method is **abstract base classes**. This allows you to define common fields and methods in a base class and reuse them in multiple child models without having a separate table for the base class.

## Abstract Base Class

An **abstract base class** in Django is a model that doesn't get its own database table but can be inherited by other models. The fields and methods of the base class are included in each child model's table.

### Example: Abstract Base Class in this Project

In the following code, I have created an abstract base class `CommonInfo`, which contains common fields like `name`, `age`, and `date`. The child models `Student`, `Teacher`, and `Contractor` inherit from this base class, but they can also override or extend the fields and methods.

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    fee = models.IntegerField()
    date = None  # Overriding date field as not required for Student

class Teacher(CommonInfo):
    date = models.DateField()  # Inheriting and reusing the date field
    salary = models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField()  # Overriding date field to DateTimeField
    payment = models.IntegerField()
```

### Explanation of the Code:

- **CommonInfo**: This is the abstract base class. It contains common fields (`name`, `age`, and `date`) that will be inherited by other models. The `Meta` class has `abstract = True`, indicating that this class won't have its own table.
  
- **Student Model**: Inherits `CommonInfo` but overrides the `date` field by setting it to `None` since it's not needed for students.
  
- **Teacher Model**: Inherits `CommonInfo` and reuses the `date` field while adding a new field `salary`.

- **Contractor Model**: Inherits `CommonInfo` but overrides the `date` field with `DateTimeField` and adds a `payment` field.

### Advantages of Abstract Base Classes:

1. **Code Reusability**: Common fields and logic are defined once in the base class and reused across multiple models.
2. **Cleaner Models**: Reduces redundancy and makes the code cleaner by avoiding duplicate field definitions.
3. **Flexibility**: Each child model can override or extend the base class fields as needed, providing flexibility in how the models are defined.

## When to Use Abstract Base Classes?

- Use **abstract base classes** when you have common fields or methods that should be shared among multiple models but do not require a separate database table for the base class.

---

This project demonstrates how to achieve **model inheritance** in Django using abstract base classes, allowing for a clean, reusable, and flexible design.
