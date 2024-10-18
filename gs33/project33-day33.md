## Implementing Model Form Inheritance in Django

In this module, I implemented inheritance in Django Model Forms to reuse common fields across different forms. By inheriting from the `StudentRegisteration` form, I created a `TeacherRegisteration` form with a similar structure but different field specifications.

### 1. Base Form (`StudentRegisteration`)
The `StudentRegisteration` form is created based on the `User` model and includes the fields `student_name`, `email`, and `password`.

```
    from django import forms
    from .models import User

    class StudentRegisteration(forms.ModelForm):
        class Meta:
            model = User
        fields = ['student_name', 'email', 'password']
```

### 2. Inheriting Form (`TeacherRegisteration`)
To avoid repeating common fields (`email`, `password`), I inherited from `StudentRegisteration` and customized the fields attribute to include `teacher_name` instead of `student_name`. I used Meta inheritance to ensure consistency in model and field handling across both forms.

```
    class TeacherRegisteration(StudentRegisteration):
        class Meta(StudentRegisteration.Meta):
            fields = ['teacher_name', 'email', 'password']
```

### 3. The User Model
The `User` model defines both `student_name` and `teacher_name`, along with shared fields like `email` and `password`, which are reused across both registration forms.

```python
from django.db import models

class User(models.Model):
    student_name = models.CharField(max_length=70)
    teacher_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
```