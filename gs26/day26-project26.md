# Project: Django Form Customization: Min/Max Values, Default Inputs, and Error Management

This project focuses on creating a Django form class with various fields and attributes, demonstrating the use of different validation rules, initial values, and custom error messages.

## Overview

In this project, I created a form class named `StudentRegistration` that includes various field types such as `CharField`, `BooleanField`, `IntegerField`, and `DecimalField`. Each field demonstrates different attributes and validation options that Django provides.

## Key Features

### Field Types and Attributes:

- **CharField**: Used for text input with parameters like `min_length`, `max_length`, `strip`, `initial`, and `empty_value`.
- **BooleanField**: For accepting a checkbox input, used here with a custom label.
- **IntegerField**: Used for numeric input, with `min_value` and `max_value` validation.
- **DecimalField**: For price and rate fields, including attributes like `max_digits` and `decimal_places`.
- **Textarea Widget**: Customized with rows and columns for the `notes` field.

### Custom Error Messages:

- For the `name5` field, I replaced the default "field required" error message with a custom message: **"Enter your name"**.

## Code Snippet

```python
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5) 
    name1 = forms.CharField(max_length=8)          
    name2 = forms.CharField(strip=False)  # Extra spaces are not removed

    name3 = forms.CharField(initial="rahim")  # Default value provided
    name4 = forms.CharField(empty_value="wazir")  # Value if left empty by user
    name5 = forms.CharField(error_messages={'required': "Enter your name"})  # Custom error message
    agree = forms.BooleanField(label='I agree')
    roll = forms.IntegerField(min_value=5, max_value=40)
    
    # Price: Max digits before and after decimal places
    price = forms.DecimalField(min_value=5, max_value=4000, max_digits=4, decimal_places=1)
    
    # Rate: Simple DecimalField without max_digits or decimal_places
    rate = forms.DecimalField(min_value=5, max_value=4000)

    # Textarea with custom rows and columns
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))
```