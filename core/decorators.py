from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


def login_required(func):    
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            current_page = request.get_full_path()
            login_url = reverse('login')
            messages.info(request, _('You shoud login to see this page.'))
            return redirect(f'{login_url}?next={current_page}')
        else: return func(request, *args, **kwargs)
    return wrap

def unauthenticated_user(func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated: return func(request, *args, **kwargs)
        else: return redirect('home')
    return wrap

def superuser_only(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser: return func(request, *args, **kwargs)
        else: raise PermissionDenied()
    return wrap

def owner_only(func):
    def wrap(request, *args, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        if request.user.username != user.username:
            raise PermissionDenied()
        return func(request, *args, **kwargs)
    return wrap