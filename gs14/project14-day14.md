# Using Bootstrap Template Inheritance in Django

In this project, I integrated Bootstrap with Django's template system to create reusable and extendable templates. Here's how I did it:

### 1. Add Bootstrap CSS and JS Files

In the `base.html` template, include the Bootstrap CSS and JS files using Django's `{% static %}` tag.
Files to Include:
- **CSS**: `bootstrap.css` (for Bootstrap styling) and optionally `all.min.css` (for Font Awesome icons).
- **JS**: `jquery.js`, `popper.js`, and `bootstrap.js` (to enable Bootstrap’s interactive features).


```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Default Title{% endblock title %}</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'core/css/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'core/css/all.min.css' %}">

    <!-- Custom CSS -->
    {% block corecss %}
    <link rel="stylesheet" href="{% static 'core/css/core.css' %}?v=2">
    {% endblock corecss %}
</head>
<body>

    <nav>
        <ul>
            <li>Home</li>
            <li>About</li>
            <li>Django Course</li>
        </ul>
    </nav>

    <!-- Bootstrap Buttons -->
    <button type="button" class="btn btn-primary">Primary</button>
    <button type="button" class="btn btn-secondary">Secondary</button>

    <i class="fa-solid fa-check"></i>

    {% block content %}{% endblock content %}
    
    <!-- Bootstrap JS and jQuery -->
    <script src="{% static 'core/js/jquery.js' %}"></script>
    <script src="{% static 'core/js/bootstrap.js' %}"></script>
    <script src="{% static 'core/js/popper.js' %}"></script>
</body>
</html>
```