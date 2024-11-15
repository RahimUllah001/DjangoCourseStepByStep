
# Django Aggregation with ORM

In this project, I have demonstrated how to use Django's ORM to perform aggregate functions such as `Avg`, `Min`, `Max`, `Sum`, and `Count` on a database model.

## Models

### Student Model
The `Student` model represents a student entity with fields like name, roll number, city, marks, pass date, and admission date and time.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    passdate = models.DateField()
    admdatetime = models.DateTimeField()
```

## Views

In the `home` view, I have retrieved all student data using `Student.objects.all()` and then applied various aggregate functions using Django's `aggregate()` method. These functions include:
- `Avg`: To calculate the average marks.
- `Max`: To get the highest marks.
- `Min`: To get the lowest marks.
- `Sum`: To calculate the total marks.
- `Count`: To count the total number of marks records.

```python
from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Min, Max, Sum, Count

def home(request):
    student_data = Student.objects.all()

    average = student_data.aggregate(Avg('marks'))
    maximum = student_data.aggregate(Max('marks'))
    minimum = student_data.aggregate(Min('marks'))
    sum = student_data.aggregate(Sum('marks'))
    count = student_data.aggregate(Count('marks'))

    print(average)

    context = {'students': student_data, 'average': average, 'min': minimum, 'max': maximum, 'sum': sum, 'count': count}
    return render(request, 'home.html', context)
```

## Aggregation Results

- **Average Marks**: Calculates the average of all student marks.
- **Maximum Marks**: Finds the student with the highest marks.
- **Minimum Marks**: Finds the student with the lowest marks.
- **Sum of Marks**: Sums up the marks of all students.
- **Count of Marks**: Counts the total number of students' marks entries.

### Output Example

In the `home.html` template, you can display the results of these aggregates as follows:

```html
<h1>Student Aggregate Data</h1>
<p>Average Marks: {{ average.marks__avg }}</p>
<p>Maximum Marks: {{ max.marks__max }}</p>
<p>Minimum Marks: {{ min.marks__min }}</p>
<p>Total Marks: {{ sum.marks__sum }}</p>
<p>Total Students Count: {{ count.marks__count }}</p>
```

## Conclusion

By using Django's ORM aggregation functions, we can easily perform database-level calculations and retrieve summarized data efficiently without having to write raw SQL queries.