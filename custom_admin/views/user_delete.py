from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

def user_delete_view(reqeust, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(reqeust, 'کاربر با موقیت حذف شد.')
    return redirect('user-list')