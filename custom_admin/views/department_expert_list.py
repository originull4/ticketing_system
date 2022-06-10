from custom_admin.imports import render, redirect, Department, get_object_or_404


def department_expert_list_view(request, id):
    department = get_object_or_404(Department, pk=id)
    context = {
        'department': department,
        'experts': department.experts.all()
    }
    return render(request, 'custom_admin/department_expert_list.html', context)