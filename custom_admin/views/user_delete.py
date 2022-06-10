from custom_admin.imports import *
from django.utils.translation import gettext as _


def user_delete_view(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    messages.success(request, _('user deleted successfully.'))
    return redirect('user-list')