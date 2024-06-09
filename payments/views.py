from django.shortcuts import render

# Create your views here.
def payment_manage(request):
    """ View for manage the payments"""
    return render(request, "payment_manage.html")