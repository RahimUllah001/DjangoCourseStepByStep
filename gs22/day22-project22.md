# Project 22:  Loop through form fields and form hidden fields  in Django
```python
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput)
```

##  Template for Form Rendering
The form is rendered in the **HTML template** in several ways:

### Rendering the Entire Form
- `{{ form }}`: This renders the entire form, including visible and hidden fields.

### Looping Through Fields
- `{% for field in form %}`: This loop renders all form fields individually, including both visible and hidden fields.

### Rendering Visible Fields Only
- `{% for field in form.visible_fields %}`: This loop is used to render only the visible fields in the form, such as `name`, `email`, and `mobile`.

### Rendering Hidden Fields Only
- `{% for field in form.hidden_fields %}`: This loop is used to render only the hidden fields like the `key` field.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <form action="" method="get">
        {{ form }}

        {% for field in form %}
            {{ field }}
        {% endfor %}

        <input type="submit" value="Submit">
        <br><br>
        <hr>

        {% for field in form.visible_fields %}
            {{ field }}
        {% endfor %}

        {% for field in form.hidden_fields %}
            {{ field }}
        {% endfor %}

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```