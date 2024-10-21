# Messages Framework in Django
In your project gs34, you've successfully implemented two key features:

1. **Basic Django Messages**: TheI've shown how to display simple messages to users using Django's messaging framework, providing feedback like success and information.

2. **Dynamic CSS Styling for Messages**: You’ve enhanced the messaging system by applying dynamic styles based on message tags, making messages more visually distinct (e.g., red for success, green for info).

---

## Key Features

### 1. Basic Django Messages
I utilized Django's built-in messaging framework to provide feedback messages to users. E.g after submitting a form, users get messages indicating whether the action was successful or if further steps are required.

In the view, messages are added like this:

```python
from django.shortcuts import render
from .forms import StudentRegisteration
from django.contrib import messages

def reg(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)  
        if fm.is_valid():
            fm.save()
            # Add success message
            messages.add_message(request, messages.SUCCESS, 'Your account has been created successfully')   # i can use this way also fr message
            # Add info message
            messages.info(request, 'Now you can login.')    # i can use this way also fr message ==> shortcut
    else:
        fm = StudentRegisteration()
    
    return render(request, 'enroll/userregisteration.html', {'form': fm})
```

### Code Explanation:
- **Message Display**: Messages are displayed with a simple loop, where the CSS class is dynamically set based on the message tag. This allows different styles to be applied to different types of messages, making them visually distinct.
  
- **CSS Styling**: Success messages are styled in red, while info messages are styled in green. This makes it easy for users to distinguish different types of feedback at a glance, improving the user experience.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Message Display</title>
    <style>
        .success {
            color: red;
        }
        .info {
            color: green;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>

    <!-- Dynamic message display based on tags -->
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