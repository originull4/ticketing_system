from custom_admin.imports import Department, redirect, get_object_or_404, messages, User
from django.utils.translation import gettext as _


def department_expert_delete_view(request, expert_id, department_id):
    department = get_object_or_404(Department, pk=department_id)
    expert = get_object_or_404(User, pk=expert_id)
    department.experts.remove(expert)

    messages.info(request, _('expert was deleted from department successfully.'))
    return redirect('department-expert-list', department_id)