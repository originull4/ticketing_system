from custom_admin.imports import *

def department_create_view(request):
    errors = []
    form = {}
    staff_users = User.objects.filter(is_staff=True)
    if request.method == 'POST':
        form = request.POST
        if Department.objects.filter(name=form['name']).exists():
            errors.append('دپارتمان با این نام قبلا ثبت شده است.')
        
        if len(errors) == 0:
            try:
                Department.objects.create(**form)
                messages.success(request, 'دپراتمان با موفقیت ایجاد شد.')
            except Exception as ex:
                errors.append(ex)
    context = {'errors': errors, 'form': form, 'staff_users': staff_users}
    return render(request, 'custom_admin/department_create.html', context)