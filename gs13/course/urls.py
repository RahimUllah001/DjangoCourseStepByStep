from django.urls import path
from . import views


print("lllll")
urlpatterns = [
    path('learndj/',views.learn_django)
]
