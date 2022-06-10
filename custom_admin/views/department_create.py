from custom_admin.imports import *
from django.utils.translation import gettext as _


def department_create_view(request):
    errors = []
    form = {}
    experts = User.objects.filter(is_staff=True)
    if request.method == 'POST':
        form['name'] = request.POST['name']
        form['description'] = request.POST['description'].strip()
        form['admin'] = int(request.POST['admin'])
        if Department.objects.filter(name=form['name']).exists():
            errors.append(_('department with this name is already exist.'))
        
        if len(errors) == 0:
            try:
                dep = Department()
                dep.admin = User.objects.get(pk=form['admin'])
                dep.name = form['name']
                dep.description = form['description']
                dep.save()
                messages.success(request, _('department created successfully.'))
                return redirect('department-list')
            except Exception as ex:
                errors.append(ex)
    context = {'errors': errors, 'form': form, 'experts': experts}
    return render(request, 'custom_admin/department_create.html', context)