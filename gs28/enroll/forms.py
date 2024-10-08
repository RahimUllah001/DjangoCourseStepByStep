from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField( )         
    password = forms.CharField(widget=forms.PasswordInput)        
    rpassword = forms.CharField(label='Password(again)' ,widget=forms.PasswordInput)        


    def clean(self):
        clean_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']

        if valpwd != valrpwd:
            raise forms.ValidationError("password does not match")