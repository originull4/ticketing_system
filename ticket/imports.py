from django.shortcuts import render, redirect, get_object_or_404
from ticket.models import Department, Ticket, TicketReply
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import gettext
from core.decorators import owner_only

from django.urls import path
from ticket.views.ticket_create import ticket_create
from ticket.views.ticket_follow import ticket_follow
from ticket.views.ticket_detail import ticket_detail
from ticket.views.ticket_reply_create import ticket_reply_create
from ticket.views.ticket_list import ticket_list
from ticket.views.ticket_close import ticket_close