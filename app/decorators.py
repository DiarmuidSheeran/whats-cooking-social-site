from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """
    Decorator for view that redirects authenticated
    users to the 'index' page.
    If the user is not authenticated,
    the original view function is executed.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

