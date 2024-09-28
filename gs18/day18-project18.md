# Django Project: Using the list_display Property of the ModelAdmin Class for Customizing the Admin Interface

## 1. **Created Django Project**
To create the Django project named **gs18**, run the following command:

```bash
django-admin startproject gs17
```

## 2. **Created Application: enroll**
Inside the project, create an application named enroll:

```bash
python manage.py startapp enroll
```

## 3. **Installed Application**
Add the enroll application to the INSTALLED_APPS section in the settings.py file.

## 4. **Created Template Folder**
Create a templates folder inside the enroll application for HTML templates.

## 5. **Model Definition**
In the models.py file of the enroll application, define the Student model:

```python
class Student(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=60)
    stupass = models.CharField(max_length=60)
```

## 6. **Creating Migrations**
To create migrations for the model, run the following command:

```bash
python manage.py makemigrations
```

This will generate the following SQL in the migration file:

```sql
CREATE TABLE "enroll_student" (
    "stuemail" varchar(60) NOT NULL, 
    "stuid" integer NOT NULL PRIMARY KEY, 
    "stuname" varchar(70) NOT NULL, 
    "stupass" varchar(60) NOT NULL
);
```

## 7. **Applying Migrations**
Run the migration command to apply the SQL and create the table in the database:

```bash
python manage.py migrate
```

## 8. **Views Implementation**
### View for All Students
To retrieve all student data from the database, write the following function in views.py:

```python
def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/studetails.html', {'stu': stud})
```

### View for Single Student
To retrieve a specific student's data from the database:

```python
def single_stu_info(request):
    stud = Student.objects.get(pk=3)
    return render(request, 'enroll/single_student_detail.html', {'stu': stud})
```

## 9. **Ways to View Data**
You can view the rendered data in three ways:
1. Through the template in the browser.
2. Through the SQLite DB Browser.
3. Through the Django Admin interface.

For this, create a superuser using the command:
```bash
python manage.py createsuperuser
```
Then give a name, email, and password.

## 10. **Customizing Object Representation**
Instead of using the `__str__` method to display a meaningful representation of the Student object in the admin interface, I used the `list_display` property. Here's how I set it up:

In `admin.py`:

```python
from django.contrib import admin
from enroll.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'stuname', 'stupass', 'stuemail')
```
