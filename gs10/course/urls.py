from django.urls import path
from . import views


urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('dt/', views.showing_date_time_template),
    path('numformat/', views.filter_for_float__number_format),
    path('if/',views.if_st),
    path('loops/',views.loops),
    path('flv/',views.forloop_varaibles),
    path('ndf/',views.nested_loop_and_dict),
    path('kv/',views.passing_key_value)
]