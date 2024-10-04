from django import forms

class StudentRegisteration(forms.Form):
#   When we have not avaliable field for something then we make its widget
    name = forms.CharField(widget=forms.PasswordInput)
    name1 = forms.CharField(widget=forms.Textarea)
    name2 = forms.CharField(widget=forms.FileInput)
    name3 = forms.CharField(widget=forms.CheckboxInput)
    name4 = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1','id':'uniqueid'})) 
  