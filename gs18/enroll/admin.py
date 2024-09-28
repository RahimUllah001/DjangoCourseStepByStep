from django.contrib import admin
import django.db
from enroll.models import Student
# Register your models here.
'''
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stupass','stuemail')

admin.site.register(Student,StudentAdmin)
'''

# the above commented way or the below
# here i use decorator   

@admin.register(Student)        

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stupass','stuemail')
