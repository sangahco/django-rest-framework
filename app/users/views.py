from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables

from .forms import CustomUserChangeForm, CustomUserCreationForm

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('apps:index'))

@login_required
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # display blank registration form
        form = CustomUserCreationForm()
    else:
        # process completed form.
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('apps:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def edit_user(request):
    user = User.objects.get(pk=request.user.pk)
    if request.method != 'POST':
        form = CustomUserChangeForm(instance=user)
    else:
        form = CustomUserChangeForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('apps:index'))

    context = {'form': form}
    return render(request, 'users/edit_user.html', context)
