## Configuring Django ModelForm for Custom Student Registration Form with Field Selection and Exclusion

In this module, I've created a `StudentRegisteration` form using Django's `ModelForm`. This form is linked to the `User` model and demonstrates three ways to configure which fields are displayed and managed by the form:

### 1. Explicit Fields List
Specific fields (`name`, `password`, `email`) can be listed, which limits the form to only these fields and allows for changing their order.

```python
fields = ['name', 'password', 'email']
```
### 2. All Fields
Using fields = '__all__', the form will include all attributes from the model.

```python
fields ='__all__
```

### 3. Field Exclusion
The exclude parameter excludes specified fields, allowing all other fields to be included automatically.
```python
exclude = ['email']
```