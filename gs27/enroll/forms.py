from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField() 
    email = forms.EmailField( )         
    password = forms.CharField(widget=forms.PasswordInput)        
    
    '''
    #custom validation on specific filed 
    def clean_name(self):       
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more han or equal to 4 character')
        return valname

    '''
    #custom validation on whole form
    def clean(self):       #custom validation on whole form
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 4:
            raise forms.ValidationError('Enter more han or equal to 4 character')

        if len(valemail) < 10:
            raise forms.ValidationError('Email should be or equal to 10 character')
        return valname
    

    #Explanation of this line cleaned_data = super().clean()
    # Preserve the Default Cleaning Process: When you override the clean method, calling super().clean() 
    # ensures that any built-in validation logic (such as type checks or required field checks) provided by Django is executed before your custom validation.
    #  This prevents you from accidentally bypassing or removing the default cleaning behavior that Django handles internally.


