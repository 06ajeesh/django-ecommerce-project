 
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib import messages


def is_log_in(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            messages.warning(request, "Please Login")
            return redirect('login_user')
    return wrapper