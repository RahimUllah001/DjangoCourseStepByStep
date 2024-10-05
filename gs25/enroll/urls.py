from django.urls import path
from . import views

urlpatterns = [
    path('registeration/', views.showformdata),  
    path('formsubmitted/', views.on_submission), 
]
