""" view when the user is Auth."""
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from classes.models import Booking
from .models import Profile
from .forms import UserProfileForm, BookingForm, MembershipForm


@login_required
def profile(request):
    """Display Profile page for the Right User"""
    profile_model = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=request.user)


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
    return render(request, 'profile.html',
                  {'from_profile': form_profile,
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
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_booking(request, booking_id):
    """Delete Booked class"""
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()

        messages.success(request, 'Booking deleted successfully.')

    except Exception as e:
        messages.error(request, f'Error deleting booking: {str(e)}')

    # Redirige a la página de perfil después de eliminar o en caso de error
    return redirect('my_profile')


@login_required
def edit_booking(request, booking_id):
    """change selected class"""
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


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
