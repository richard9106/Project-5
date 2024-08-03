from django.urls import path
from . import views, web_hooks


urlpatterns = [
    path('pay_membership/<int:membership_id>', views.checkout, name='pay_membership'),
]
