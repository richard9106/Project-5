# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Profile
from memberships.models import Membership, Subscription
from .forms import CustomSignupForm
import stripe



def checkout(request, membership_id):
    """Render payment page and handle POST request"""
    membership = Membership.objects.get(id=membership_id)
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    profile_form = CustomSignupForm(request.POST or None)
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=int(membership.price) * 100,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        if profile_form.is_valid():
            # Save the user using the form's save method
            user = profile_form.save(request)
            
            # Retrieve and update profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.first_name = profile_form.cleaned_data['first_name']
            profile.last_name = profile_form.cleaned_data['last_name']
            profile.email = profile_form.cleaned_data['email']
            profile.phone_number = profile_form.cleaned_data.get('phone_number', '')
            profile.my_memberships = membership
            profile.active = True
            profile.save()

            
            # Specify the backend for allauth
            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'


            # Log the user in
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            
            # Create subscription
            Subscription.objects.create(user=user, membership=membership)
            
            # Redirect to profile page
            messages.success(request, "!! CONGRATS welcome to Iron Heaven Fitness Family")
            return redirect('my_profile')  # Replace 'profile_page_url' with the actual URL name of the profile page
        else:
            messages.error(request, "There were errors in the form. Please correct them.")
    
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing.")
    
    return render(request, 'pay_membership.html', {
        'profile_form': profile_form,
        'membership': membership,
        'STRIPE_PUBLISHABLE_KEY': stripe_public_key,
        'client_secret': intent.client_secret,
    })
    

# def checkout_products(request):