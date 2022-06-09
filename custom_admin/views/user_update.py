from custom_admin.imports import *

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
        if is_english(form['username']) == False:
            errors.append('نام کاربری باید انگلیسی باشد.')
        if len(form['username']) < 5:
            errors.append('نام کاربری حداقل باید شامل ۵ حرف باشد.')
            
        if len(errors) == 0:
            try:
                User.objects.filter(pk=id).update(**form)
                messages.success(request, 'تغییرات ذخیره شد.')
                return redirect('user-list')
            except Exception as ex:
                errors.append(ex)
    print(errors)

    return render(request, 'custom_admin/user_update.html', {'user_object': user, 'errors': errors})