from ticket.imports import path, ticket_create, ticket_follow, ticket_detail, ticket_reply_create


urlpatterns = [
    path('create/', ticket_create, name='ticket-create'),
    path('follow/', ticket_follow, name='ticket-follow'),
    path('<int:id>/detail/', ticket_detail, name='ticket-detail'),
    path('<int:id>/reply/', ticket_reply_create, name='ticket-reply-create')
]