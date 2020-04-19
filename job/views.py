from django.contrib.auth import login as auth_login
from annoying.functions import get_object_or_None
from django.shortcuts import render, redirect, HttpResponse, reverse
from .forms import SignUpForm, LevelCategoryForm, ResourceCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from job.models import Job, Resource, Level, Comments, LevelUpCategory, ResourceCategory
import json
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

    def get(self, *args, **kwargs):
        categoryid = self.kwargs.get("id", None)
        if categoryid is not None:
            category = get_object_or_None(LevelUpCategory, id=categoryid)
            if category is None:
                return redirect("levelup")
        return super(ShowAllLevelView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LevelCategoryForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        categoryid = self.kwargs.get("id", None)
        if categoryid is not None:
            category = get_object_or_None(LevelUpCategory, id=categoryid)
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_at')



@method_decorator(login_required, name='dispatch')
class ShowAllResourcesView(ListView):
    model = Resource
    context_object_name = 'resources'
    template_name = 'remote-resources.html'
    paginate_by = 10

    def get(self, *args, **kwargs):
        categoryid = self.kwargs.get("id", None)
        if categoryid is not None:
            category = get_object_or_None(ResourceCategory, id=categoryid)
            if category is None:
                return redirect("resource")
        return super(ShowAllResourcesView, self).get(*args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResourceCategoryForm()
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        categoryid = self.kwargs.get("id", None)
        if categoryid is not None:
            category = get_object_or_None(ResourceCategory, id=categoryid)
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_at')
        