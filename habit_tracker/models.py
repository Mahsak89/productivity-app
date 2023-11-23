from django.db import models
from django.contrib.auth.models import User
from habits.models import Habit  # Assuming you have a 'habits' app


class HabitCompletion(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completion_date = models.DateField()

    class Meta:
        unique_together = ('owner', 'habit', 'completion_date')
