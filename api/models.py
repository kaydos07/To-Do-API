from django.db import models


class task(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        completed = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)