from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateField(default=timezone.now, blank=True)
