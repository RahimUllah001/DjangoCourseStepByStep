# Django QuerySet Methods Without New QuerySets

This project demonstrates various Django QuerySet methods that do not return new QuerySets. These methods allow for creating, updating, deleting, and retrieving objects without creating a fresh QuerySet. Below are examples of the methods used in the project with descriptions of their functionality.

## Model: Student

The `Student` model contains fields like `name`, `roll`, `city`, `marks`, `pass_date`, and `admission_date`. Here's the model used in this project:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admission_date = models.DateTimeField()
```

## Views: Methods Not Returning New QuerySets

The `home` view demonstrates the usage of methods that do not return new QuerySets. Instead, they operate on individual objects or sets of objects.

```python
from django.shortcuts import render
from .models import Student

def home(request):
    # Retrieve a specific student by primary key (ID)
    # students_data = Student.objects.get(pk=3)

    # Retrieve the first student in the database
    # students_data = Student.objects.first()

    # Retrieve the last student in the database
    # students_data = Student.objects.last()

    # Retrieve the latest student based on a specific field (pass_date)
    # students_data = Student.objects.latest('pass_date')

    # Retrieve the earliest student based on a specific field (pass_date)
    # students_data = Student.objects.earliest('pass_date')

    # Check if the student data exists
    # students_data = Student.objects.all()
    # print("Student data exists:", students_data.exists())

    # Create a new student object
    # students_data = Student.objects.create(name='ummehani', roll=999, city='bannu', marks=100, pass_date='2020-5-6')

    # Get or create a student record (if it exists, retrieve it; otherwise, create a new one)
    # students_data = Student.objects.get_or_create(name='ummehani', roll=999, city='bannu', marks=100, pass_date='2020-5-6')

    # Update a specific student's record
    # students_data = Student.objects.filter(id=10).update(name='ummehaniwazir', roll=888)

    # Update multiple records at once
    # students_data = Student.objects.filter(marks=100).update(city='prizeholder')

    # Update or create a student (if it exists, update; otherwise, create a new one)
    # students_data, created = Student.objects.update_or_create(city='swat', defaults={'city':'Bannu'})

    # Create multiple student objects at once using bulk_create
    objs = [
        Student(name='Umer1', roll=1111, city='Peshawar', marks=999, pass_date='2020-5-6'),
        Student(name='Umer2', roll=1112, city='Peshawar', marks=999, pass_date='2020-5-6'),
        Student(name='Umer3', roll=1113, city='Peshawar', marks=999, pass_date='2020-5-6'),
    ]

    students_data = Student.objects.bulk_create(objs)

    # Delete a specific student by primary key (ID)
    # students_data = Student.objects.filter(pk=10).delete()

    # Delete all student records
    # students_data = Student.objects.all().delete()

    # Count the total number of students in the database
    students_data = Student.objects.all()
    print("Total Students:", students_data.count())

    return render(request, 'school/home.html', {'students': students_data})
```

## Template: Displaying Student Data

The `home.html` file renders the student data in a tabular format.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Data</title>
    <style>
        table, th, td {
            border: solid 1px black;
            padding: 8px;
        }
    </style>
</head>
<body>

    <h1>Student Data</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Roll Number</th>
                <th>City</th>
                <th>Marks</th>
                <th>Pass Date</th>
                <th>Admission Date</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.roll }}</td>
                <td>{{ student.city }}</td>
                <td>{{ student.marks }}</td>
                <td>{{ student.pass_date }}</td>
                <td>{{ student.admission_date }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

</body>
</html>
```

## How to Run the Project

1. Clone the repository.
2. Run `pip install -r requirements.txt` to install the required dependencies.
3. Run `python manage.py migrate` to apply migrations.
4. Start the development server using `python manage.py runserver`.
5. Access the app at `http://127.0.0.1:8000/`.

## Methods Used

- `get()`: Retrieves a single object by its primary key.
- `first()`: Retrieves the first object from the QuerySet.
- `last()`: Retrieves the last object from the QuerySet.
- `latest(field_name)`: Retrieves the latest object based on the given field.
- `earliest(field_name)`: Retrieves the earliest object based on the given field.
- `exists()`: Checks if the QuerySet contains any results.
- `create()`: Creates a new object and saves it to the database.
- `get_or_create()`: Retrieves an object or creates it if it doesn't exist.
- `update()`: Updates the selected object(s).
- `update_or_create()`: Updates an existing object or creates a new one.
- `bulk_create()`: Inserts multiple objects at once into the database.
- `delete()`: Deletes the selected object(s).
- `count()`: Counts the number of objects in the QuerySet.
