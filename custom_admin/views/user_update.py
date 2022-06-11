from custom_admin.imports import get_object_or_404, User, is_english, messages, redirect, render, login_required, superuser_only
from django.utils.translation import gettext as _


@login_required
@superuser_only
def user_update_view(request, id):
    errors = []
    form = {}
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form['username'] = request.POST.get('username')
        form['first_name'] = request.POST.get('first_name')
        form['last_name'] = request.POST.get('last_name')
        form['email'] = request.POST.get('email')
        form['is_active'] = True if request.POST.get('is_active') == 'on' else False
        form['is_staff'] = True if request.POST.get('is_staff') == 'on' else False
        form['is_superuser'] = True if request.POST.get('is_superuser') == 'on' else False

        if User.objects.exclude(pk=id).filter(username=form['username']).exists():
            errors.append(_('this username is taken, try with other username.'))
        if is_english(form['username']) == False:
            errors.append(_('username must be in english.'))
        if len(form['username']) < 5:
            errors.append(_('username must be 5 characters at least.'))
            
        if len(errors) == 0:
            try:
                User.objects.filter(pk=id).update(**form)
                messages.success(request, _('user updated successfully.'))
                return redirect('user-list')
            except Exception as ex:
                errors.append(ex)
    print(errors)

    return render(request, 'custom_admin/user_update.html', {'user_object': user, 'errors': errors})