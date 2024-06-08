""" membership view"""
from django.shortcuts import render
from .models import Membership


def membership_list(request):
    """ render view for membersjip list"""
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})



