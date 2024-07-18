from django.urls import path
from . import views

urlpatterns = [
    path('',views.classes_list, name="classes_list" ),
    path('reserve/<int:class_id>/', views.reserve_class, name='reserve_class'),
]
