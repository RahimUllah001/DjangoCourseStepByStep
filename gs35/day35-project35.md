
# Project 35: Dynamic Message Styling and Message Levels in Django

In this project, we demonstrate how to apply dynamic CSS styling based on message tags in Django and how to work with different message levels.

## HTML Template

Here’s the HTML form and message display section:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <style>
        .success {
            color: green;
        }
        .info {
            color: blue;
        }
        .debug {
            color: orange;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>

    {% comment %} Dynamic CSS based on message tags {% endcomment %}
    {% if messages %}
        {% for message in messages %}
            <p {% if message.tags %} class="{{ message.tags }}" {% endif %}>
                {{ message }}
            </p>
        {% endfor %}
    {% endif %}
</body>
</html>
```

### Explanation:
- The form uses the `{{ form.as_p }}` Django template tag to render fields with paragraph tags.
- The messages are displayed within a `p` tag, with dynamic CSS classes applied based on message tags (like `success`, `info`, and `debug`).
- The styles for different message tags (`.success`, `.info`, and `.debug`) are defined in the `<style>` section.

## Django View (views.py)

The view handles user registration, shows success or debug messages, and also demonstrates how to retrieve the current message level.

```python
from django.shortcuts import render
from .forms import StudentRegisteration
from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)  
        if fm.is_valid():
            fm.save()
            # Display info level message
            messages.info(request, 'Now you can log in.')

            # Print current message level in the console
            print("Message level: ", messages.get_level(request))

            # Display debug message
            messages.debug(request, "This is a debug message.")

            # Set the message level to DEBUG and display another debug message
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "This is a new debug message after setting level.")
    else:
        fm = StudentRegisteration()
    
    return render(request, 'enroll/userregisteration.html', {'form': fm})
```

### Explanation:
- `messages.info(request, 'Now you can log in.')`: Displays an informational message.
- `messages.get_level(request)`: Retrieves and prints the current message level.
- `messages.set_level(request, messages.DEBUG)`: Changes the message level to `DEBUG` so future debug messages are displayed.
- Messages are rendered dynamically in the template with corresponding CSS classes.

## Dynamic CSS Styling

The messages are displayed with dynamic styles depending on their tags, which can be one of the following levels in Django:
- `debug`
- `info`
- `success`
- `warning`
- `error`

Each message tag can be associated with a specific style (like color), as defined in the `<style>` section of the HTML.

## Conclusion

In this project, we learned how to:
- Use Django’s messaging framework to display messages with different levels.
- Dynamically style messages based on their tags using CSS.
- Change and retrieve message levels.
