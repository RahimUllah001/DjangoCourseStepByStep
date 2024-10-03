from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    # required=False, ==> this field will not be required must and disabled=True means no one can edit this filed cannot meansenter value,
    name1 = forms.CharField(label="Your Name",label_suffix="::",initial="rahim",required=False,disabled=True,help_text="Max 50 characters")
  