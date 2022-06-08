from django.shortcuts import render
from core.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')