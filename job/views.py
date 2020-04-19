from django.contrib.auth import login as auth_login
from annoying.functions import get_object_or_None
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from job.models import Job
# Create your views here.
def error_404_view(request, exception):
    return redirect('home')


def home(request):
    return render(request, 'index.html')


class ShowAllJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'remote-jobs.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Job.objects.all().count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date')

