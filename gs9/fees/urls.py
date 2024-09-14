from django.urls import path

from . import views

urlpatterns = [
    path('feedj/',views.fee_django),
    path('feepy/',views.fee_python),
]