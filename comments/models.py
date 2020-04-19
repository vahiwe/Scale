from django.db import models
from django.contrib.auth.models import User
from level.models import Level
# Create your models here.
class Comments(models.Model):
    comment = models.TextField(default='')
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return '{}'.format(self.comment)