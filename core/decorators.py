from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404

def login_required(func):    
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            current_page = request.get_full_path()
            login_url = reverse('login')
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
        else: raise Http404("شما اجازه ندارید.")
    return wrap