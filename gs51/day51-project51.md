# Django QuerySet API: Methods That Return New QuerySets
### **Theory of Queryset and Django ORM is in the last**
This project demonstrates various Django QuerySet methods that return new QuerySets. These methods are used to retrieve, filter, and combine data while creating new QuerySets. Below are examples of the methods used and the SQL queries they generate.

## Models: Student and Teacher

We have two models, `Student` and `Teacher`, in this project, each with several fields.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()

class Teacher(models.Model):
    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
```

## Views: QuerySet Methods Returning New QuerySets

The `home` view demonstrates the use of various QuerySet methods that return new QuerySets. SQL queries are shown in comments.

```python
from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from django.db.models.functions import Lower

def home(request):
    # Retrieve all students (returns a new QuerySet)
    # students_data = Student.objects.all()
    # SQL: SELECT * FROM "school_student";

    # Filter students with specific marks
    # students_data = Student.objects.filter(marks=77)
    # SQL: SELECT * FROM "school_student" WHERE "school_student"."marks" = 77;

    # Exclude students by pass_date
    # students_data = Student.objects.exclude(pass_date="2024-10-06")
    # SQL: SELECT * FROM "school_student" WHERE NOT ("school_student"."pass_date" = '2024-10-06');

    # Order students by pass_date (ascending and descending)
    # students_data = Student.objects.order_by('pass_date')
    # SQL: SELECT * FROM "school_student" ORDER BY "pass_date" ASC;

    # Reverse order of students by ID and limit the results to 6
    # students_data = Student.objects.order_by('id').reverse()[:6]
    # SQL: SELECT * FROM "school_student" ORDER BY "id" DESC LIMIT 6;

    # Select specific fields with values_list (named tuples)
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    students_data = qs2.union(qs1)
    # SQL: SELECT "id", "name" FROM "school_teacher" UNION SELECT "id", "name" FROM "school_student";

    # Union, Intersection, and Difference Queries
    # students_data = qs2.union(qs1, all=True)
    # SQL: UNION ALL allows duplicates.
    
    # students_data = qs2.intersection(qs1)
    # SQL: Returns only rows common in both queries.

    # Filter using Q objects with AND and OR conditions
    # students_data = Student.objects.filter(Q(id=6) | Q(roll=112))
    # SQL: SELECT * FROM "school_student" WHERE "id" = 6 OR "roll" = 112;

    print("SQL Query:", students_data.query)
    return render(request, 'school/home.html', {'students': students_data})
```

## SQL Queries Generated

- **`all()`**: Returns all records, e.g., `SELECT * FROM "school_student";`
- **`filter()`**: Filters records based on given conditions, e.g., `SELECT * FROM "school_student" WHERE "marks" = 77;`
- **`exclude()`**: Excludes records based on conditions, e.g., `SELECT * FROM "school_student" WHERE NOT ("pass_date" = '2024-10-06');`
- **`order_by()`**: Orders records based on specified fields, e.g., `SELECT * FROM "school_student" ORDER BY "pass_date" ASC;`
- **`reverse()`**: Reverses the ordering of the QuerySet.
- **`values_list()`**: Returns tuples of selected fields, e.g., `SELECT "id", "name" FROM "school_student";`
- **`union()`**: Combines results of two QuerySets, e.g., `SELECT "id", "name" FROM "school_teacher" UNION SELECT "id", "name" FROM "school_student";`
- **`intersection()`**: Returns common records between two QuerySets.
- **`difference()`**: Returns records from one QuerySet that are not in another.
- **`Q()`**: Allows complex query filtering with AND/OR conditions.

## Template: Displaying Data

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
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

## How to Run the Project

1. Clone the repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run migrations with `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.
5. Access the app at `http://127.0.0.1:8000/`.



# QuerySet in Django

## What is a QuerySet?
In Django, a QuerySet is a collection of database queries that are executed against the database to retrieve, filter, or manipulate data. It is essentially a representation of a database query that can be used to interact with the database in an efficient way.

## Why Use QuerySets?
- **Abstraction**: QuerySets abstract the complexities of SQL queries, allowing developers to work with Python objects instead of writing raw SQL.
- **Chaining**: QuerySets are designed to be chainable. This means you can build complex queries incrementally by calling methods on a QuerySet one after another.
- **Lazy Evaluation**: QuerySets are evaluated lazily. This means that a QuerySet is not executed until it is explicitly required, which helps optimize performance by reducing unnecessary database hits.
- **Caching**: Once a QuerySet is evaluated, it caches the results. If you reuse the same QuerySet, it won’t hit the database again, improving efficiency.

## Advantages of Using QuerySets
1. **Simplicity**: They provide a simple and easy-to-use interface for database interactions, making the code more readable and maintainable.
2. **Flexibility**: QuerySets can be filtered, ordered, and sliced in a very flexible way, allowing for complex queries to be built without extensive code.
3. **Integration**: QuerySets integrate seamlessly with Django's ORM, making it easier to manage database models and their relationships.
4. **Database-agnostic**: QuerySets are independent of the underlying database system. This allows for easy switching between different database backends without changing the code.

## Django ORM (Object-Relational Mapping)
Django's ORM is a powerful feature that allows developers to interact with the database using Python code instead of SQL. It maps database tables to Python classes, and QuerySets are the way to retrieve and manipulate data in these tables. The ORM handles the conversion between Python objects and database records, making database operations more intuitive and less error-prone.

By leveraging QuerySets and the ORM, developers can focus on building their applications without getting bogged down by SQL queries and database management details.