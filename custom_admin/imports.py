from django.shortcuts import render, redirect, get_object_or_404
from ticket.models import Department
from django.contrib.auth.models import User
from django.contrib import messages
from core.functions import is_english

from django.urls import path
from custom_admin.views.dashboard import dashboard_view
from custom_admin.views.user_list import user_list_view
from custom_admin.views.user_update import user_update_view
from custom_admin.views.user_delete import user_delete_view
from custom_admin.views.department_create import department_create_view
from custom_admin.views.department_list import department_list_view
from custom_admin.views.department_update import department_update_view
from custom_admin.views.department_delete import department_delete_view