from django.contrib import admin
from django.urls import path, include
from .views import home_view, test_view
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('test/', test_view),
    path('', RedirectView.as_view(pattern_name='home')),

    path('account/', include('account.urls')),
    path('adminc/', include('custom_admin.urls')),
    path('ticket/', include('ticket.urls'))
]