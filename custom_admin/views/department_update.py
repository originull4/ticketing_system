from custom_admin.imports import (
    Department, User, get_object_or_404, render, redirect, messages, login_required, superuser_only
)
from django.utils.translation import gettext as _


@login_required
@superuser_only
def department_update_view(request, id):
    department = get_object_or_404(Department, pk=id)
    experts = User.objects.filter(is_staff=True)
    form = {}
    errors = []
    
    if request.method == 'POST':
        form['name'] = request.POST['name']
        form['description'] = request.POST['description'].strip()
        form['admin'] = int(request.POST['admin'])
        if Department.objects.exclude(pk=id).filter(name=form['name']).exists():
            errors.append(_('department with this name is already exist.'))
        
        if len(errors) == 0:
            try:
                department.admin = User.objects.get(pk=form['admin'])
                department.name = form['name']
                department.description = form['description']
                department.save()
                messages.success(request, _('department created successfully.'))
                return redirect('department-list')
            except Exception as ex:
                errors.append(ex)
    context = {
        'experts': experts,
        'department': department,
        'form': form,
        'errors': errors
    }

    return render(request, 'custom_admin/department_update.html', context)