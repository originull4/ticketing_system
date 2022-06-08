from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from core.functions import is_english, checkbox_to_bool


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
            errors.append('این نام کربری قبلا ثبت شده است. با یک نام کاربری دیگر امتحان کنید.')
        elif is_english(form['username']) == False:
            errors.append('نام کاربری باید انگلیسی باشد.')
        elif len(form['username']) < 5:
            errors.append('نام کاربری حداقل باید شامل ۵ حرف باشد.')
        else:
            User.objects.filter(pk=id).update(**form)
            messages.success(request, 'تغییرات ذخیره شد.')
            return redirect('user-list')



    return render(request, 'custom_admin/user_update.html', {'user_object': user})