# Template Inheritance in Django

## What is Template Inheritance?

In Django, template inheritance allows me to define a base layout that can be shared across multiple pages. It helps avoid code duplication by letting individual templates (like those for specific pages) reuse common elements like headers, footers, and navigation. By using template inheritance, I ensure that changes to the layout only need to be made in one place, the base template, making it easier to maintain consistent styling across the project.

## How Do I Achieve Template Inheritance?

### Base Template (`base.html`):

I start by creating a base template that contains the general structure of the webpage. This includes the HTML `<head>`, `<body>`, and common elements like the navigation bar, and placeholders (blocks) for content that will be filled by other templates.

### Extending the Base Template:

In individual templates, I extend the base template using `{% extends "path/to/base.html" %}`. This makes the child template inherit everything from the base template.

### Using Blocks:

In the base template, I define areas that can be overridden by child templates using the `{% block block_name %}` and `{% endblock %}` tags. Each child template can then override these blocks to insert its own content.

### Super Blocks (`block.super`):

In cases where I want to keep part of the content from the parent block while adding my own content, I use `{{ block.super }}`. This allows me to inherit the content of the parent block and append or modify it with specific content for the child template.

## Example Breakdown

### Base Template (`base.html`):

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}By Default value{% endblock title %}</title>

    {% block corecss %}
    <link rel="stylesheet" href="{% static "core/css/core.css" %}?v=2">
    {% endblock corecss %}
</head>
<body>
    <nav>
        <ul>
            <li>home</li>
            <li>about</li>
            <li>django course</li>
        </ul>
    </nav>

    {% block content %}{% endblock content %}
    {% block content1 %}{% endblock content1 %}
</body>
</html>
```
I create a base template that includes default blocks like title, corecss, content, and content1. These blocks will be overridden in child templates.

### Child Template (home.html):

```html
{% extends "core/base.html" %}

{% block title %}{{ block.super }}+Home{% endblock title %}

{% block content %}
I am the new home page.
{% endblock content %}
```

In home.html, I extend the base template. I override the title block and use {{ block.super }} to include the title from the parent template while adding "+Home" to it. I override the content block to add specific content for the home page.

Another Child Template (courseinfo.html):
```html
{% extends "core/base.html" %}
{% load static %}

{% block corecss %}
{{ block.super }}
<link rel="stylesheet" href="{% static "course/css/course.css" %}">
{% endblock corecss %}

{% block title %}Django{% endblock title %}

{% block content %}
I am the course Django page.
{% endblock content %}

```
In courseinfo.html, I extend the base template and also load static files. I override the corecss block to add custom CSS for this specific page while keeping the parent styles using {{ block.super }}. The title block is overridden with a specific title, Django, which completely replaces the parent title.

CSS Inheritance Example:
**I have core styles in core.css:**

```css
body {
    background-color: darkgoldenrod;
}

h2 {
    color: aliceblue;
}

nav {
    color: rgb(233, 11, 11);
}

```
**In course.css, I override the nav color:**
```css
nav {
    color: rgb(61, 25, 204);
}
This structure ensures that I use global styles defined in core.css while allowing specific pages like the course page to have their own styles.

Conclusion
By using template inheritance, I ensure that all pages share a common layout while allowing flexibility for each individual page to have its own unique content. The use of {% extends %}, {% block %}, and {{ block.super }} helps maintain a balance between reusability and customization, making the project easier to manage and scale.


# Project Flow:
I'm implementing a structure where a core application handles the base layout (like `base.html`), and other application templates extend that core. This is a great approach to centralize and maintain consistent styling and layout across the entire project.

By using this method, I ensure that the base template and core styles (defined in the core application) are shared across multiple applications. Each specific application, like the course app or home page, can then extend the core layout and override certain blocks (such as `title`, `content`, or `corecss`) to customize its content or styles while still inheriting the base structure.

## Core Application:
- It holds the base layout in `base.html` with default blocks for `title`, CSS, and content.
- I define global styles in `core.css` and use `{% block corecss %}` in `base.html` to allow child templates to inject their own styles.

## Home Page (from core app):
- The `home.html` extends `base.html` and appends a new title to the base title using `block.super`, and content blocks. It also inherits the base CSS (`core.css`) without adding additional styles.
- I also demonstrated how to combine the parent title with a specific title for the home page using `block.super`.

## Course Page (from course app):
- The `courseinfo.html` also extends `base.html` but adds its own CSS via the `{% block corecss %}` block. This block preserves the core CSS and adds course-specific styles (`course.css`).
- The title block is overridden to display "Django" without using `block.super`, meaning it fully replaces the parent block's content.
