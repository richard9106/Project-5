"""View for clases """
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import Profile
from .models import GymClass, Booking
from .forms import GymClassForm
from django.http import JsonResponse


def classes_list(request):
    """ Pass all the classes with edit form """
    classes = GymClass.objects.all()
    return render(request, 'classes_list.html', {'classes': classes})


@login_required
def reserve_class(request, class_id):
    """ Manage reservation"""
    if request.method == 'POST':
        gym_class = get_object_or_404(GymClass, id=class_id)
        user_profile = Profile.objects.get(user=request.user)

        # Check if the user has already reserved this class
        if Booking.objects.filter(user_booking=user_profile, gym_class=gym_class).exists():
            messages.error(request, 'You have already reserved this class.')
            return redirect('classes_list')
        
        # Create a new reservation
        reservation = Booking.objects.create(user_booking=user_profile, gym_class=gym_class)
        reservation.save()
        messages.info(request, 'Class reserved successfully.')
        
        return redirect(reverse('classes_list'))
    
    messages.error(request, 'Invalid request method.')
    return redirect(reverse('classes_list'))


def edit_class(request, class_id):
    """ Edit the details of a gym class """
    gym_class = get_object_or_404(GymClass, id=class_id)
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = GymClassForm(request.POST, request.FILES, instance=gym_class)
            if form.is_valid():
                form.save()
                messages.success(request, 'Class updated successfully.')
                return redirect('classes_list')  # Redirect after saving
            else:
                messages.error(request, 'Check your form  something is not right.')
                return redirect('edit_class')
                
        elif 'delete' in request.POST:
            gym_class.delete()
            messages.success(request, 'Class deleted successfully.')
            return redirect('classes_list')  # Redirect after deletion
        elif 'cancel' in request.POST:
            return redirect('classes_list')  # Redirect on cancel

    else:
        form = GymClassForm(instance=gym_class)

    return render(request, 'edit_class.html', {'form': form, 'gym_class': gym_class})