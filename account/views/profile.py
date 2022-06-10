from account.imports import render, login_required

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')