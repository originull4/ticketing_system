from django.contrib import admin
from django.urls import path, include
from .views import home_view
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('', RedirectView.as_view(pattern_name='home')),

    # path('', include('auth.urls'))
]