from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="my_profile"),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_membership/', views.change_membership, name='change_membership'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    
]