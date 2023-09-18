from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


class Task(models.Model):
    # Define choices for task state
    state_choices = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    # Define choices for task priority
    priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    state = models.CharField(
        max_length=15,
        choices=state_choices,
        default='open',
    )

    priority = models.CharField(
        max_length=10,
        choices=priority_choices,
        default='Medium',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
