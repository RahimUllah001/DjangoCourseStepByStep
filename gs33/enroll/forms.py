from django import forms
from .models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']

class TeacherRegisteration(StudentRegisteration):
    class Meta(StudentRegisteration.Meta):
        fields = ['teacher_name', 'email', 'password']