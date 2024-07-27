# memberships/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.conf import settings
from django.contrib import messages
from .models import Membership
from .forms import SignupForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def membership_list(request):
    """Render view for membership list"""
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})

@csrf_exempt
def process_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data
            membership = form.cleaned_data['membership_id']
            user = form.save()
            login(request, user)

            # Stripe payment processing
            try:
                charge = stripe.Charge.create(
                    amount=int(membership.price * 100),  # Stripe amount is in cents
                    currency='usd',
                    description=f"Charge for {membership.name}",
                    source=request.POST['stripeToken']
                )
                # Save order information or any other necessary data
                messages.success(request, 'Thank you for signing up! Your payment was successful.')
                return redirect('profile')  # Assumes you have a profile URL configured
            except stripe.error.StripeError:
                # Handle error
                messages.error(request, 'There was an error processing your payment. Please try again.')
                return render(request, 'memberships/signup.html', {'form': form, 'membership': membership})
        else:
            membership = form.cleaned_data.get('membership_id')
            return render(request, 'memberships/signup.html', {'form': form, 'membership': membership})
    else:
        return render(request, 'membership_checkout.html')

def membership_checkout(request):
    return render(request, 'membership_checkout.html')
