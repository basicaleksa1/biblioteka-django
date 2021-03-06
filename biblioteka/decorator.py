from django.http import HttpResponse
from django.shortcuts import redirect


def unauthentificated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('biblioteka:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allow_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Nije dozvoljen pristup')
        return wrapped_func
    return decorator


def admin_only(view_func):
        def wrapped_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'korisnik':
                return redirect('biblioteka:korisnik')

            if group == 'admin':
                return view_func(request, *args, **kwargs)
        return wrapped_function
