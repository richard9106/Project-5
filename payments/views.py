from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Order, OrderLineItem
from profiles.models import Profile
from products.models import Product
from memberships.models import Membership
import stripe

@login_required
def initiate_payment(request):
    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        original_bag = request.POST.get('original_bag')

        # Create the order
        order = Order.objects.create(
            user_profile=user_profile,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            original_bag=original_bag,
        )

        # Create order line items for products
        for item in request.session.get('bag', []):
            product = get_object_or_404(Product, id=item['product_id'])
            order_line_item = OrderLineItem(
                order=order,
                product=product,
                product_size=item.get('product_size', ''),
                quantity=item['quantity'],
                lineitem_total=product.price * item['quantity'],
            )
            order_line_item.save()

        # Add a line item for membership if selected
        membership_id = request.POST.get('membership_id')
        if membership_id:
            membership = get_object_or_404(Membership, id=membership_id)
            order_line_item = OrderLineItem(
                order=order,
                product=membership,
                quantity=1,
                lineitem_total=membership.price,
            )
            order_line_item.save()

        # Calculate the grand total
        order_total = sum(item.lineitem_total for item in order.lineitems.all())
        order.order_total = order_total
        order.grand_total = order_total
        order.save()

        # Create Stripe session
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.product.name,
                        },
                        'unit_amount': int(item.product.price * 100),
                    },
                    'quantity': item.quantity,
                } for item in order.lineitems.all()
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/'),
            cancel_url=request.build_absolute_uri('/payments/cancel/'),
        )

        order.stripe_pid = session.id
        order.save()

        return redirect(session.url, code=303)

    return render(request, 'initiate_payment.html')


@login_required
def payment_success(request):
    # Aquí puedes agregar la lógica para marcar la membresía como pagada
    user = request.user
    user.profile.membership_paid = True
    user.profile.save()
    return render(request, 'payment_success.html')

@login_required
def payment_cancel(request):
    return render(request, 'payment_cancel.html')
