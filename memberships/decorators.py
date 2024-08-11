from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 
                           'Sorry, you cannot access this page as a member.')
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
