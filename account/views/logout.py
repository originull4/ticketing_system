from account.imports import *

def logout_view(request):
    logout(request)
    return redirect('login')