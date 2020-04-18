from django.db import models

# Create your models here.
class Jobs(models.Model):
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