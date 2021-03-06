from custom_admin.imports import render, User, Department, get_object_or_404, login_required, superuser_only


@login_required
@superuser_only
def department_expert_new_view(request, id):
    department = get_object_or_404(Department, pk=id)
    experts = User.objects.filter(is_staff=True).exclude(id__in=department.experts.all())
    
    context = {
        'experts': experts,
        'department': department
    }
    return render(request, 'custom_admin/department_expert_new.html', context)