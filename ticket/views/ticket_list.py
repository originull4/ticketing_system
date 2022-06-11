from ticket.imports import Ticket, render, Department, get_object_or_404


def ticket_list(request):
    tickets = Ticket.objects.all()
    ticket_name = request.GET.get('ticket_search')
    department = request.GET.get('department')
    if ticket_name:
        tickets = tickets.filter(title__icontains=ticket_name)
    if department:
        tickets = tickets.filter(department=department)
    return render(request, 'ticket/ticket-list.html', {'tickets': tickets})
