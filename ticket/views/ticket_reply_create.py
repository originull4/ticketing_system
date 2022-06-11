from django.http import HttpResponseNotFound
from ticket.imports import Ticket, TicketReply, get_object_or_404, redirect, messages, gettext as _


def ticket_reply_create(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    if request.method == 'POST':
        try:
            reply = TicketReply()
            reply.ticket = ticket
            reply.user = request.user
            reply.body = request.POST.get('body').strip()
            reply.save()
            messages.success(request, _('reply created successfully.'))
        except Exception as ex:
            messages.error(request, _(ex))

        return redirect('ticket-detail', ticket.id)
    return HttpResponseNotFound()
    


