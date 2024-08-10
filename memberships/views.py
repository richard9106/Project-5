"""Render Membership page"""

from django.shortcuts import render
from .models import Membership
from .decorators import unauthenticated_user


@unauthenticated_user
def membership_list(request):
    """Render view for membership list"""
    memberships = Membership.objects.all()
    user = request.user
    
    return render(request, 'membership_list.html', 
                  {'memberships': memberships,
                   'user':user,
                   })

