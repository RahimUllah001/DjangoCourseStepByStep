from django.urls import path
from . import views

urlpatterns = [
    path('cit/',views.check_templates_inside_application),
]