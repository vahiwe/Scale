from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    pid = models.AutoField(primary_key=True)  # Primary ID
    id = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, default='')
    epoch = models.CharField(max_length=255, default='')
    date = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=255, default='')
    position = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    url = models.CharField(max_length=255, default='')
    visible = models.BooleanField(default=False)

class Resource(models.Model):
    CATEGORIES = (
        ('OPEN', 'OPEN'),
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
    )
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    url = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resource')


class Level(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=255, default='')
    salary = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='level')

class Comments(models.Model):
    comment = models.TextField(default='')
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
