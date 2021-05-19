from django.db import models


class Todo(models.Model):
    check = models.BooleanField(default=False)
    title = models.CharField(max_length=35)
    description = models.TextField()
    time = models.IntegerField(default=60)

