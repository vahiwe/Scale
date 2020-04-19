from django.contrib import admin
from .models import ResourceCategory, Resource
# Register your models here.
admin.site.register(Resource)
admin.site.register(ResourceCategory)