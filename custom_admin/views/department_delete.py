from custom_admin.imports import *

def department_delete_view(request, id):
    department = get_object_or_404(Department, pk=id)
    department.delete()
    messages.success(request, 'دپارتمان با موفقیت حذف شد.')
    return redirect('department-list')