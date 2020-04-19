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
    url = models.TextField(default='')
    visible = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.position)



