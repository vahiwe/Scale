from django.contrib import admin
from .models import Job, Resource, Level, Comments
# Register your models here.
admin.site.register(Job)
admin.site.register(Resource)
admin.site.register(Level)
admin.site.register(Comments)