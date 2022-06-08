from django.urls import path
from account.views.signup import signup_view
from account.views.login import login_view
from account.views.logout import logout_view
from account.views.profile import profile_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]