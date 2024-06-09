"""View for user profile manage"""
from django.shortcuts import render


def register(request):
    """view for user profile"""
    return render(request, 'register.html')