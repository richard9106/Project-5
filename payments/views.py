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
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    profile_form = CustomSignupForm(request.POST or None)
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=int(membership.price) * 100,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        if profile_form.is_valid():
            username = profile_form.cleaned_data['username']
            email = profile_form.cleaned_data['email']
            password = profile_form.cleaned_data['password1']
            first_name = profile_form.cleaned_data.get('first_name', '')
            last_name = profile_form.cleaned_data.get('last_name', '')
            phone_number = profile_form.cleaned_data.get('phone_number', '')
            birthday = profile_form.cleaned_data.get('birthday', None)

            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Retrieve and update profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.email = email
            profile.phone_number = phone_number
            profile.birthday = birthday
            profile.my_memberships = membership
            profile.active = True
            profile.save()
            
            # Specify the backend for allauth
            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'


            # Log the user in
            login(request, user)
            
            # Create subscription
            Subscription.objects.create(user=user, membership=membership)
            
            # Redirect to profile page
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
    
