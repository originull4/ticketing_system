from custom_admin.imports import *
from django.utils.translation import gettext as _

def department_delete_view(request, id):
    department = get_object_or_404(Department, pk=id)
    department.delete()
    messages.success(request, _('department deleted successfully.'))
    return redirect('department-list')