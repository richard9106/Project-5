from django.urls import path
from . import views

urlpatterns = [
    path('',views.classes_list, name="classes_list" ),
]
