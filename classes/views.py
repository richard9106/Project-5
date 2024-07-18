"""View for clases """
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GymClass, Booking
from profiles.models import Profile


def classes_list(request):
    """ Pass all the classes"""
    classes = GymClass.objects.all()  # Obtener todas las clases desde el modelo
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
        messages.success(request, 'Class reserved successfully.')
        
        return redirect(reverse('classes_list'))
    
    messages.error(request, 'Invalid request method.')
    return redirect(reverse('classes_list'))