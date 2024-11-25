from django.contrib import admin
import django.db
from .models import ExamCenter,Student
# Register your models here.


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city','name', 'roll']