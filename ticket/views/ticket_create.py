from django.shortcuts import redirect
from ticket.imports import render, Department, get_object_or_404, Ticket, messages, gettext as _, User


def ticket_create(request):
    form = {}
    errors = []
    if request.method == 'POST':
        form['title'] = request.POST.get('title')
        form['body'] = request.POST.get('body').strip()
        form['department'] = get_object_or_404(Department, pk=request.POST.get('department'))
        form['owner'] = get_object_or_404(User, pk=request.user.id)
        try:
            # new_ticekt = Ticket()
            # new_ticekt.owner = request.user
            # new_ticekt.title = form['title']
            # new_ticekt.department = form['department']
            # new_ticekt.body = form['body']
            # print(new_ticekt.closed_at)
            # new_ticekt.save()
            Ticket.objects.create(**form)
            messages.success(request, _('ticket was created successfully.'))
            return redirect('profile')
        except Exception as ex:
            errors.append[_(ex)]
    context = {
        'departments': Department.objects.all(),
        'form': form,
        'errors': errors}
    return render(request, 'ticket/ticket_create.html', context)