from datetime import time
from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title