
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import stripe
from profiles.models import Profile
from products.models import Product
from bag.contexts import bag_contents
from memberships.models import Membership, Subscription
from .forms import CustomSignupForm, OrderForm
from .models import OrderLineItem

import json



def checkout(request, membership_id):
    """Render payment membership page and handle POST request"""
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
            messages.success(request,
                             "!! CONGRATS welcome to Iron Heaven Fitness Family.")
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


@login_required
def checkout_products(request):
    """ control checkout product view"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.user_profile = profile
            order.original_bag = json.dumps(bag)
            order.save()  
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
                
            if 'bag' in request.session:
                del request.session['bag']
            messages.success(request, 'Your order has been processed correctly.You can pick up your order at your gym!!! ')
            return redirect(reverse('my_profile_with_order',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = get_object_or_404(Profile, user=request.user)
                order_form = OrderForm(initial={   
                    'first_name':profile.first_name,
                    'last_name':profile.last_name, 
                    'email':profile.user.email, 
                    'phone_number':profile.phone_number, 

                })
            except Profile.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'pay_product.html'
    context = {
        'profile':profile,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)