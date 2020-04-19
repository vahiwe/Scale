from django.contrib.auth import login as auth_login
from annoying.functions import get_object_or_None
from django.shortcuts import render, redirect, HttpResponse, reverse
from .forms import ResourceCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Resource, ResourceCategory

# Create your views here.

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
        