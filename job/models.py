from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    pid = models.AutoField(primary_key=True)  # Primary ID
    id = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, default='')
    epoch = models.CharField(max_length=250, default='')
    date = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=250, default='')
    position = models.CharField(max_length=250, default='')
    description = models.CharField(max_length=250, default='')
    url = models.CharField(max_length=250, default='')
    visible = models.BooleanField(default=False)

class Resource(models.Model):
    CATEGORIES = (
        ('OPEN', 'OPEN'),
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
    )
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250, default='')
    description = models.TextField(default='')
    url = models.CharField(max_length=250, default='')
    category = models.CharField(max_length=250, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='resource')


