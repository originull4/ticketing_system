from account.imports import logout, redirect

def logout_view(request):
    logout(request)
    return redirect('login')