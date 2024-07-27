from django.urls import path
from . import views


urlpatterns = [
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('payments/success/', views.payment_success, name='payment_success'),
    path('payments/cancel/', views.payment_cancel, name='payment_cancel'),
]
