from django.urls import path
from . import views

urlpatterns = [
    path('',views.membership_list, name='membership_list'),
     path('process_signup/', views.process_signup, name='process_signup'),
]
