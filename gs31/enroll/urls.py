from django.urls import path
from .  import views

urlpatterns = [
    # path('<my_id>/', views.show_details,name="detail"),     #But here my_id will be considered str by default if we do not specify explicitly 
    path('<int:my_id>/', views.show_details,name="detail"),    # making it integer 
    # the below is for such urls http://127.0.0.1:8000/student/4/1/
    path('<int:my_id>/<int:my_subid>/', views.show_subdetails,name="subdetail"),    # making it integer 
]