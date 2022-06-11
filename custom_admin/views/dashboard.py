from django.shortcuts import render
from core.decorators import superuser_only, login_required

@login_required
@superuser_only
def dashboard_view(request):
    return render(request, 'custom_admin/dashboard.html')