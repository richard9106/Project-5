# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import stripe
from memberships.models import Membership, Subscription



def checkout(request, membership_id):
    """render payment page"""
    membership = Membership.objects.get(id=membership_id)
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount= int(membership.price) * 100,
        currency=settings.STRIPE_CURRENCY,      
    )
    print(intent)
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing.")
    
    return render(request, 'pay_membership.html', {
        'membership': membership,
        'STRIPE_PUBLISHABLE_KEY':stripe_public_key,  # Pasa la clave pública a la plantilla
        'client_secret': intent.client_secret,
    })
    
