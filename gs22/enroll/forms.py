from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()

    key = forms.CharField(widget=forms.HiddenInput)