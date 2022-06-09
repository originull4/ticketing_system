from custom_admin.imports import *

def department_list_view(request):
    departments = Department.objects.all()
    return render(request, 'custom_admin/department_list.html', {'departments': departments})