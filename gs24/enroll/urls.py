from django.urls import path
from . import views

urlpatterns = [
    path('registeration/', views.showformdata),  # Correct spelling here
]
