from custom_admin.imports import Department, redirect, login_required, superuser_only, render


@login_required
@superuser_only
def department_list_view(request):
    departments = Department.objects.all()
    department_name = request.GET.get('department_search')
    if department_name:
        departments = departments.filter(name__icontains=department_name)        
    return render(request, 'custom_admin/department_list.html', {'departments': departments})