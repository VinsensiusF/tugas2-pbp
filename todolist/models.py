from pydoc import describe
from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)