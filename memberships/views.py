
from django.shortcuts import render
from .models import Membership


def membership_list(request):
    """Render view for membership list"""
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})
