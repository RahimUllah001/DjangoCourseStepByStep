from django.urls import path
from . import views

urlpatterns = [
    path('cif/',views.check_templates_inside_application),
]