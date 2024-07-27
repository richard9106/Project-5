from django.urls import path
from . import views

urlpatterns = [
    path('',views.membership_list, name='membership_list'),
    path('signup/', views.process_signup, name='process_signup'),
    path('membership_checkout/', views.membership_checkout, name='membership_checkout'),
]
