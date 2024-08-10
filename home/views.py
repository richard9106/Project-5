from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from products.models import Product
from classes.models import GymClass
from .forms import ContactForm

from .forms import NewsletterForm
from .models import NewsletterSubscription



def index(request):
    """ View for home page """
    products = Product.objects.all()
    classes = GymClass.objects.all()
    form = ContactForm()
    news_form = NewsletterForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Check if email already exists
            if NewsletterSubscription.objects.filter(email=email).exists():
                messages.error(request, 'You are already subscribed.')
            else:
                # Save the new subscription
                NewsletterSubscription.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')
        else:
            messages.error(request, 'No email in the newsletter')
            return redirect('home')

    return render(request, "index.html", {
        'products': products,
        'classes': classes,
        'contact_form': form,
        'news_form': news_form,
    })


def contact_view(request):
    """Manage contact form"""
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

    return render(request, 'home', {'contact_form': form})
