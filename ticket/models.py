from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    admin = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='admin')
    experts = models.ManyToManyField(User, blank=True, related_name='experts')
    name = models.CharField(verbose_name='department name', max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True,)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='replied_by', null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self) -> str:
        return self.ticket.title