from django.urls import path
from . import views

urlpatterns = [
    path('',views.payment_manage, name="payment_manage" ),
]
