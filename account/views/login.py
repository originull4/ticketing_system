from account.imports import unauthenticated_user, authenticate, login, messages, redirect, render
from django.utils.translation import gettext as _

@unauthenticated_user
def login_view(request):
    form = {}

    if request.method == 'POST':
        form = request.POST
        user = authenticate(username=form['username'], password=form['password'])

        if user:
            login(request, user)
            messages.success(request, _('you are logged in successfully.'))
            return redirect('profile')

        else:
            messages.error(request, _('username or password is wrong.'))

    return render(request, 'account/login.html', {'form': form})