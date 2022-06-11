from ticket.imports import render, Ticket, get_object_or_404


def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    context = {
        'ticket': ticket,
        'replies': ticket.replies.all(),
    }
    return render(request, 'ticket/ticket-detail.html', context)