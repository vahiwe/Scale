from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from job.models import Job, Resource, Level, Comments
# Create your views here.
def error_404_view(request, exception):
    return redirect('home')


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

def home(request):
    return render(request, 'index.html')


@method_decorator(login_required, name='dispatch')
class ShowAllJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'remote-jobs.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')

@method_decorator(login_required, name='dispatch')
class ShowAllLevelView(ListView):
    model = Level
    context_object_name = 'levels'
    template_name = 'level-up.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')


@login_required
def resource(request):
    return render(request, 'remote-resources.html')
