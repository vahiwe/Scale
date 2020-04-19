from django.contrib.auth import login as auth_login
from annoying.functions import get_object_or_None
from django.shortcuts import render, redirect, HttpResponse, reverse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('jobs')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})