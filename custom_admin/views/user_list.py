from custom_admin.imports import User, render, login_required, superuser_only


@login_required
@superuser_only
def user_list_view(request):
    users = User.objects.all()
    user_search = request.GET.get('user_search')
    if user_search:
        users = users.filter(username__icontains=user_search)
    return render(request, 'custom_admin/user_list.html', {'users': users})