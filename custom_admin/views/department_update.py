from custom_admin.imports import *

def department_update_view(request, id):
    context = {'department': get_object_or_404(Department, pk=id)}
    return render(request, 'custom_admin/department_update.html', context)