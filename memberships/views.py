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

# views.py

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        membership_form = MembershipForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and membership_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.my_memberships = membership_form.save()
            profile.save()

            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        membership_form = MembershipForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'membership_form': membership_form
    })
