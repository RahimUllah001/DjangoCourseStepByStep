# Project 27: Custom Validation in Django Forms

This project demonstrates how to implement custom validation in Django forms, both on specific fields and across the entire form. Below is the `StudentRegistration` form class with custom validation logic.

## Code Implementation

```python
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    '''
    # Custom validation on a specific field
    def clean_name(self):       
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more than or equal to 4 characters')
        return valname
    '''
    # Custom validation on the entire form
    def clean(self):
        cleaned_data = super().clean()  # Preserve the default cleaning process
        valname = self.cleaned_data.get('name')
        valemail = self.cleaned_data.get('email')

        # Validate the 'name' field to ensure it has at least 4 characters
        if valname and len(valname) < 4:
            raise forms.ValidationError('Enter more than or equal to 4 characters')

        # Validate the 'email' field to ensure it has at least 10 characters
        if valemail and len(valemail) < 10:
            raise forms.ValidationError('Email should be at least 10 characters long')

        return cleaned_data
```

## Explanation

### 1. clean_name 
The `clean_name` method is an example of custom validation for a specific field in Django forms. It validates the `name` field by checking if the length is less than 4 characters. If it is, it raises a validation error.

The method is currently commented out, as the validation is done on the entire form in this project, but this serves as an example of field-level validation.

### 2. clean Method
The `clean` method is used to implement form-level custom validation. It validates multiple fields together, which allows checking for relationships between fields or applying complex validation rules.

In this example, both the `name` and `email` fields are validated:

- The `name` field must have at least 4 characters.
- The `email` field must have at least 10 characters.

**Line Explanation: `cleaned_data = super().clean()`**

This line ensures that the built-in validation logic provided by Django (such as required fields, type checks, etc.) is executed before custom validation is applied.  
Calling `super().clean()` retains the default behavior of the form, avoiding the risk of overriding or missing any essential validation that Django handles internally.

### 3. Widgets
The `password` field uses the `PasswordInput` widget to ensure the input is masked in the form.
