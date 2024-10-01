from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    name1 = forms.CharField(initial="rahim")
   