from ticket.imports import (
    path, ticket_create, ticket_follow, ticket_detail, ticket_reply_create, ticket_list, ticket_close
)


urlpatterns = [
    path('create/', ticket_create, name='ticket-create'),
    path('follow/<str:username>/', ticket_follow, name='ticket-follow'),
    path('list/', ticket_list, name='ticket-list'),
    path('<int:id>/detail/', ticket_detail, name='ticket-detail'),
    path('<int:id>/close/<str:username>/', ticket_close, name='ticket-close'),
    path('<int:id>/reply/', ticket_reply_create, name='ticket-reply-create'),
]