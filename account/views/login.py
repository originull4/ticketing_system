from account.imports import *

@unauthenticated_user
def login_view(request):
    form = {}

    if request.method == 'POST':
        form = request.POST
        user = authenticate(username=form['username'], password=form['password'])

        if user:
            login(request, user)
            messages.success(request, 'شما با موفقیت وارد شدید')
            return redirect('profile')

        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')

    return render(request, 'account/login.html', {'form': form})