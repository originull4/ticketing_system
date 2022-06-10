import django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from core.decorators import unauthenticated_user, login_required
from core.functions import is_english
from django.urls import path
from account.views.signup import signup_view
from account.views.login import login_view
from account.views.logout import logout_view
from account.views.profile import profile_view
from django.utils.translation import gettext