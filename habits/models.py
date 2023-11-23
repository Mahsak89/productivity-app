from django.contrib.auth.models import User
from django.db import models


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tracking_period = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
