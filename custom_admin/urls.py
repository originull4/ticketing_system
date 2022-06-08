from django.urls import path
from custom_admin.views.dashboard import dashboard_view
from custom_admin.views.user_list import user_list_view
from custom_admin.views.user_update import user_update_view
from custom_admin.views.user_delete import user_delete_view



urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    
    path('users/list/', user_list_view, name='user-list'),
    path('users/<int:id>/update/', user_update_view, name='user-update'),
    path('users/<int:id>/delete/', user_delete_view, name='user-delete'),
]