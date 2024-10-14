from django import forms
from django.core import validators

class StudentRegisteration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter your name'}) #here i provided custom error message as the defailt rror message is the field is required 
    email = forms.EmailField( error_messages={'required':'Enter your email'})         
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password'})        

