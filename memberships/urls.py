from django.urls import path
from . import views

urlpatterns = [
    path('', membership_list, name='membership_list'),
]
