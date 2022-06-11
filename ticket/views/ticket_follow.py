from ticket.imports import render, Ticket
from core.decorators import owner_only


@owner_only
def ticket_follow(request, username):
    context = {
        'tickets': Ticket.objects.filter(owner=request.user).order_by('created_at')
    }
    print(context['tickets'])
    return render(request, 'ticket/ticket_follow.html', context)