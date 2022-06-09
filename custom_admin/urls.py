from custom_admin.imports import *


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    
    path('users/list/', user_list_view, name='user-list'),
    path('users/<int:id>/update/', user_update_view, name='user-update'),
    path('users/<int:id>/delete/', user_delete_view, name='user-delete'),
    
    path('departments/list/', department_list_view, name='department-list'),
    path('departments/create/', department_create_view, name='department-create'),
    path('departments/<int:id>/update/', department_update_view, name='department-update'),
    path('departments/<int:id>/delete/', department_delete_view, name='department-delete'),
]