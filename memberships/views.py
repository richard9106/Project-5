from django.shortcuts import render
from .models import Membership


def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})



