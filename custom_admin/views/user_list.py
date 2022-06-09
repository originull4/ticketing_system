from custom_admin.imports import *


def user_list_view(request):
    users = User.objects.all()
    user_search = request.GET.get('user_search')
    if user_search:
        users = users.filter(username__icontains=user_search)
    return render(request, 'custom_admin/user_list.html', {'users': users})