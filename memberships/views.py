""" membership view"""
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Membership, Advantage
from .forms import SignupForm


def membership_list(request):
    """ render view for membersjip list"""
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})



@csrf_exempt
def process_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data
            membership_id = form.cleaned_data['membership_id']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            card_number = form.cleaned_data['card_number']
            expiry_date = form.cleaned_data['expiry_date']
            address = form.cleaned_data['address']
            
            # Create a new user (this example is simplified)
            user = User.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, password=card_number)
            
            # Handle payment processing (this is a placeholder)
            # You should integrate with a real payment gateway

            return redirect('memberships')
        else:
            return render(request, 'memberships/memberships.html', {'form': form})
    else:
        return redirect('memberships')