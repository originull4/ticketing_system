from custom_admin.imports import *

def user_delete_view(reqeust, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(reqeust, 'کاربر با موقیت حذف شد.')
    return redirect('user-list')