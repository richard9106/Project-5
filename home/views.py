from django.shortcuts import render
from products.models import Product
from classes.models import GymClass


# Create your views here.
def index(request):
    """ View for home page"""
    products = Product.objects.all()
    classes  = GymClass.objects.all()
    return render(request, "index.html",{
        'products':products,
        'classes':classes,
    })