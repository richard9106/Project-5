""" view when the user is Auth."""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from classes.models import Booking
from payments.models import Order, OrderLineItem
from .models import Profile
from .forms import UserProfileForm, BookingForm, MembershipForm


@login_required
def profile(request, order=None):
    """Display Profile page for the Right User"""
    profile_model = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=request.user.profile)
    edit_booking_form = BookingForm(request.POST, instance=profile_model)

    # get all the order
    user_orders = profile_model.orders.all()

    if order:
        order_item = get_object_or_404(user_orders, order_number=order)
    else:
        order_item = user_orders.first() if user_orders.exists() else None

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST,
                                       request.FILES,
                                       instance=profile_model)
        if form_profile.is_valid():
            profile_model.completed_info = True
            form_profile.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your profile was update successfully")
            return redirect('profile')
        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Something has gone wrong check your form')
    
    return render(request, 'profile.html',{
                'form_profile': form_profile,
                'form_booking': edit_booking_form,
                'form_member': MembershipForm,
                'order_item': order_item,
                'user_orders': user_orders,
                })


@login_required
def delete_profile(request, user):
    """ Deletes the user's account and logs them out."""
    profile_model = get_object_or_404(Profile, user=request.user)
    if request.user:
        profile_model.delete()
        user.delete()
        logout(request)
        messages.add_message(
                request,
                messages.SUCCESS,
                "Your account has been successfully deleted.")
        return redirect(reverse('home'))
    else:
        messages.add_message(
                request,
                messages.WARNING,
                "Something has gone wrong.")
        return redirect(reverse('profile'))


@login_required
def edit_profile(request):
    """Edit profile info"""
    profile = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form_profile.is_valid():
            profile.active = True
            form_profile.save()  # Save without modifying `membership`
            messages.success(request, "Your profile was updated successfully.")
            return redirect(reverse('my_profile'))
        else:
            print("Errores del formulario:", form_profile.errors)
            messages.error(request, 'Error updating profile.')

    return redirect(reverse('my_profile'))


@login_required
def delete_booking(request, booking_id):
    """Delete Booked class"""
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()

        messages.warning(request, 'Booking deleted successfully.')

    except Exception as e:
        messages.error(request, f'Error deleting booking: {str(e)}')

    # Redirect to profile page after deleting or in case of error
    return redirect('my_profile')


@login_required
def change_membership(request):
    """Change our subscription"""
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            # Process form data and update user's membership
            profile = get_object_or_404(Profile, user=request.user)
            profile.my_memberships = form.cleaned_data['membership']
            profile.save()
            return redirect('profile')
    else:
        form = MembershipForm()

    return render(request, 'change_membership.html', {'form': form})


@login_required
def cancel_membership(request):
    """Cancel membership, delete user profile, and redirect to home"""
    if request.method == 'POST':
        # Get the user's profile and delete it
        profile = get_object_or_404(Profile, user=request.user)
        user = profile.user
        profile.delete()
        user.delete()
        messages.success(request,
                         "Your membership has been cancelled \
                             and your profile has been deleted.")
        return redirect('home')

    return render(request, 'cancel_membership.html')