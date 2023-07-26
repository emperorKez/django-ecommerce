from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from user.models import User
from user.forms import LoginForm, RegisterForm

# register view
def register_view(request):
    pass

# login view
def login_view(request):
    pass

# logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('core:home')

