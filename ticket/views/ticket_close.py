from ticket.imports import redirect, Ticket, get_object_or_404, owner_only, messages, gettext as _


@owner_only
def ticket_close(request, id, username):
    try:
        ticket = get_object_or_404(Ticket, pk=id)
        ticket.closed = True
        ticket.save()
        messages.success(request, _('message was closed successfully.'))
    except Exception as ex:
        messages.error(request, _(ex))
    return redirect('ticket-detail', id)