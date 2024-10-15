from django.contrib import admin
from .models import User
# Register your models here.

# if i not register momy model here it will save data but will notshow in database
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')