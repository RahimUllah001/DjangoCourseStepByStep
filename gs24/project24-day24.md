# Project 24 - Django Form Custom Widgets

In this project, I worked on creating a custom form using Django's `forms.Form` class, where I applied different widgets to the form fields to control how they are rendered in the browser.

## Code

```python
from django import forms

class StudentRegistration(forms.Form):
    # When we do not have a predefined field type, we can customize it using widgets
    name = forms.CharField(widget=forms.PasswordInput)
    name1 = forms.CharField(widget=forms.Textarea)
    name2 = forms.CharField(widget=forms.FileInput)
    name3 = forms.CharField(widget=forms.CheckboxInput)
    name4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'somecss1', 'id': 'uniqueid'}))
```
## Explanation

- **Password Field (`name`)**: A password input widget is used to hide the characters.
- **Textarea (`name1`)**: A large text box for multi-line input.
- **File Input (`name2`)**: Allows the user to upload a file.
- **Checkbox (`name3`)**: A checkbox input widget.
- **Text Input with Custom Attributes (`name4`)**: A standard text input field with custom CSS class and unique ID.
