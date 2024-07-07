"""View for clases """
from django.shortcuts import render, redirect, get_object_or_404
from .models import GymClass


def classes_list(request):
    """ Pass all the classes"""
    classes = GymClass.objects.all()  # Obtener todas las clases desde el modelo
    return render(request, 'classes_list.html', {'classes': classes})

def reserve_class(request, class_id):
    # Logic to reserve the class
    # Here you can implement the logic for class reservation based on the received class_id
    return HttpResponse("Reserve Class view placeholder")