from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Membership
from django.contrib.auth.models import User

def membership_list(request):
    """Render view for membership list"""
    memberships = Membership.objects.all()
    user = request.user
    
    return render(request, 'membership_list.html', 
                  {'memberships': memberships,
                   'user':user,
                   })

