from gettext import gettext
from django.shortcuts import render
from django.utils.translation import gettext as _
from ticket.imports import render, gettext as _, Ticket


def home_view(request):
    return render(request, 'core/home.html')

def test_view(request):
    output = _("Welcome to my site.")
    return render(request, 'core/test.html', {'output': output})
