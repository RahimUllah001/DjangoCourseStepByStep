from django import forms

from .models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'password','email']     # can to set any field or to change their order

        # fields = '__all__'            #used for setting all atributes

        exclude = ('name',)     #used for setting all fields  excludong the given tuple = list ==> exclude = ['name'] 
        