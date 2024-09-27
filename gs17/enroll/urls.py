from django.urls import path

from . import views


urlpatterns = [
    path('stu/',views.studentinfo),
    path('single/',views.single_stu_info)
]