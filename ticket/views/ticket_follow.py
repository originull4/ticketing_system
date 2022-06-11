from ticket.imports import render, Ticket


def ticket_follow(request):
    context = {
        'tickets': Ticket.objects.filter(owner=request.user).order_by('created_at')
    }
    print(context['tickets'])
    return render(request, 'ticket/ticket_follow.html', context)