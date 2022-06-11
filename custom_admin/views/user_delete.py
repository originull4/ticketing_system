from custom_admin.imports import User, get_object_or_404, messages, redirect, login_required, superuser_only
from django.utils.translation import gettext as _


@login_required
@superuser_only
def user_delete_view(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(request, _('user deleted successfully.'))
    return redirect('user-list')