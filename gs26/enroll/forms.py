from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField(min_length=5) 
    name1 = forms.CharField( max_length=8)          
    name2 = forms.CharField(strip=False)        # by defult it is true as it remove the xtra spaces  

    name3 = forms.CharField(initial="rahim")       #this will put the value before the user put value   
    name4 = forms.CharField(empty_value="wazir")         #this will give value if the user does not give any value 
    name5 = forms.CharField(error_messages={'required':"Enter your name"})  #by default message of this is "filed required" whne we put field empty and try to submit but here i change the message to enter your name       
    agree = forms.BooleanField(label='I agree')
    roll = forms.IntegerField(min_value=5,max_value=40)
    # for price ==> max-digits means there only would be 4 digits in total before decimal and after decial ,, decimal places means there should be only one digit after decimal
    price = forms.DecimalField(min_value=5,max_value=4000,max_digits=4,decimal_places=1)
    rate = forms.DecimalField(min_value=5,max_value=4000)       #only have thses attributes
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))      #this will give me a textarea of 3 rows and cols