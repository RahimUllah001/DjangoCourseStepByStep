from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField() 
    password = forms.CharField(widget=forms.PasswordInput)
    