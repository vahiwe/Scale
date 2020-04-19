from django.contrib import admin
from .models import Job, Resource, Level, Comments, ResourceCategory, LevelUpCategory
# Register your models here.
admin.site.register(Job)
admin.site.register(Resource)
admin.site.register(Level)
admin.site.register(Comments)
admin.site.register(ResourceCategory)
admin.site.register(LevelUpCategory)