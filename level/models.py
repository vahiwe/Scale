from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LevelUpCategory(models.Model):
    name = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='levelupcategory')

    def __str__(self):
        return '{}'.format(self.name)

class Level(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    category = models.ForeignKey(
        LevelUpCategory, on_delete=models.CASCADE, related_name='levels')
    salary = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='level')

    def __str__(self):
        return '{}'.format(self.title)
