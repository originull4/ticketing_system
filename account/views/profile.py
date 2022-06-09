from account.imports import *

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')