from account.imports import unauthenticated_user, is_english, User, login, messages, render, redirect
from django.utils.translation import gettext as _

@unauthenticated_user
def signup_view(request):
    errors = []
    form = {}
    if request.method == 'POST':
        form = request.POST
        if User.objects.filter(username=form['username']).exists():
            errors.append(_('this username is taken, try with other username.'))
        if is_english(form['username']) == False:
            errors.append(_('username must be in english.'))
        if len(form['username']) < 5:
            errors.append(_('username must be 5 characters at least.'))
        if form['password1'] != form['password2']:
            errors.append(_('password and password confirm must be equal.'))
        if(len(form['password1']) < 8):
            errors.append(_('password must be 8 characters at least.'))
        if len(errors) == 0:
            try:
                user = User.objects.create_user(username=form['username'], password=form['password1'])
                login(request, user)
                messages.success(request, _('your registration is done and you are loged in.'))
                return redirect('profile')
            except Exception as ex:
                errors.append(ex)
    return render(request, 'account/signup.html', {'errors': errors, 'form': form})