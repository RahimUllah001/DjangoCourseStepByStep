from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
