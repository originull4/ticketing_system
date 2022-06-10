from custom_admin.imports import Department, User, get_object_or_404, redirect


def department_expert_add_view(request, department_id, expert_id):
    department = get_object_or_404(Department, pk=department_id)
    expert = get_object_or_404(User, pk=expert_id)
    department.experts.add(expert)
    return redirect('department-expert-new', department.id)