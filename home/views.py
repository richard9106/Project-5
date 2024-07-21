from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from products.models import Product
from classes.models import GymClass
from .forms import ContactForm


# Create your views here.
def index(request):
    """ View for home page"""
    products = Product.objects.all()
    classes  = GymClass.objects.all()
    form = ContactForm()
    return render(request, "index.html",{
        'products':products,
        'classes':classes,
        'contact_form': form,
    })
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f"Contact Form Submission from {name}",
                message,
                email,
                ['your_email@example.com'],  # Replace with your email or the email where you want to receive the contact form messages
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # Replace 'home' with the name of your homepage URL
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'contact_form': form})