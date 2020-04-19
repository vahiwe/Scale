from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resourcecategory')

    def __str__(self):
        return '{}'.format(self.name)

class Resource(models.Model):
    CATEGORIES = (
        ('OPEN', 'OPEN'),
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
    )
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, default='')
    company = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    url = models.TextField(default='')
    category = models.ForeignKey(
        ResourceCategory, on_delete=models.CASCADE, related_name='resources')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resource')

    def __str__(self):
        return '{}'.format(self.title)

