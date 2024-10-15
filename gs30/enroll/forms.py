from django import forms
from django.core import validators
import django.db
from .models import User
# here i am making form from model

class StudentRegisteration(forms.ModelForm):        #in the below line i am going to implement extra vlaiddater
    # name = forms.CharField(max_length=50,min_length=5) #this thing will override the below properties of the name which u have defined in meta class 
    class Meta:
        model = User 
        fields = ['name','email','password']

        # as i have not used form api so in the followinf way i wll make labels error messages etc
        labels = {'name':'plz enter your name', 'password':'Enter Your password','email': 'plz enter your email'}
        error_messages = {
            'name':{'required':'Name filed is must'}
        }

        widgets = {+
            'password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':"write your name here"}),
        }