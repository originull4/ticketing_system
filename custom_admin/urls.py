from custom_admin.imports import (
    path, dashboard_view, user_list_view, user_update_view, department_list_view, user_delete_view,department_create_view,
    department_update_view, department_delete_view, department_expert_list_view, department_expert_new_view,
    department_expert_delete_view, department_expert_add_view
)


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    
    path('users/list/', user_list_view, name='user-list'),
    path('users/<int:id>/update/', user_update_view, name='user-update'),
    path('users/<int:id>/delete/', user_delete_view, name='user-delete'),
    
    path('departments/list/', department_list_view, name='department-list'),
    path('departments/create/', department_create_view, name='department-create'),
    path('departments/<int:id>/update/', department_update_view, name='department-update'),
    path('departments/<int:id>/delete/', department_delete_view, name='department-delete'),
    
    path('departments/<int:id>/experts/list/', department_expert_list_view, name='department-expert-list'),
    path('departments/<int:id>/experts/new/', department_expert_new_view, name='department-expert-new'),
    path('departments/<int:department_id>/experts/<int:expert_id>/delete/', department_expert_delete_view, name='department-expert-delete'),
    path('departments/<int:department_id>/experts/<int:expert_id>/add/', department_expert_add_view, name='department-expert-add'),
]