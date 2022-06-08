from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from core.decorators import unauthenticated_user
from core.functions import is_english

@unauthenticated_user
def signup_view(request):
    errors = []
    form = {}
    if request.method == 'POST':
        form = request.POST
        if User.objects.filter(username=form['username']).exists():
            errors.append('این نام کربری قبلا ثبت شده است. با یک نام کاربری دیگر امتحان کنید.')
        if is_english(form['username']) == False:
            errors.append('نام کاربری باید انگلیسی باشد.')
        if len(form['username']) < 5:
            errors.append('نام کاربری حداقل باید شامل ۵ حرف باشد.')
        if form['password1'] != form['password2']:
            print('password')
            errors.append('رمز عبور و تایید رمز عبور باید یکسان باشند.')
        if(len(form['password1']) < 8):
            errors.append('رمز عبور حداقل باید شامل ۸ کارکاتر باشد.')
        if len(errors) == 0:
            try:
                user = User.objects.create_user(username=form['username'], password=form['password1'])
                login(request, user)
                messages.success(request, 'ثبت نام شما انجام و وارد شدید.')
                return redirect('profile')
            except Exception as ex:
                errors.append(ex)
    return render(request, 'account/signup.html', {'errors': errors, 'form': form})