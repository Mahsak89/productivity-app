from django.db import models
from datetime import date
from categories.models import Category
from django.contrib.auth.models import User
from tags.models import Tag


class Task(models.Model):

    priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    startdate = models.DateField(default=date.today)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=priority_choices,
        default='Medium',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
