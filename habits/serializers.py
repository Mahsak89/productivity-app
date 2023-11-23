from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Habit
        fields = '__all__'

    def validate_tracking_period(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Tracking period must be a positive integer.")
        return value
