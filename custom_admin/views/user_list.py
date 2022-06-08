from django.shortcuts import render
from django.contrib.auth.models import User


def user_list_view(request):
    users = User.objects.all()
    return render(request, 'custom_admin/user_list.html', {'users': users})