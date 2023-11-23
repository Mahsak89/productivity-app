from rest_framework import serializers
from .models import HabitCompletion


class HabitCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCompletion
        fields = '__all__'
