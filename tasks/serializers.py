from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Task
from states.models import State
import datetime


class TaskSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    state_id = serializers.SerializerMethodField()
    states_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_state_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            state = State.objects.filter(
                owner=user, task=obj
            ).first()
            return state.id if state else None
        return None

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate(self, data):
        """
        Custom validation to check if deadline is not set before startdate.
        """
        startdate = data.get('startdate')
        deadline = data.get('deadline')

        if startdate and deadline:
            # Ensure startdate is a datetime object
            if isinstance(startdate, datetime.date):
                startdate = datetime.datetime.combine(
                    startdate, datetime.datetime.min.time())

            # Ensure deadline is a datetime object
            if isinstance(deadline, datetime.date):
                deadline = datetime.datetime.combine(
                    deadline, datetime.datetime.min.time())

            # Compare the corrected objects
            if deadline < startdate:
                raise serializers.ValidationError(
                    "Deadline cannot be set before the start date.")

        return data

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'category',
            'title', 'description', 'created_at', 'updated_at', 'startdate',
            'deadline', 'priority', 'state_id', 'states_count'
        ]


class TaskDetailSerializer(TaskSerializer):

    category = serializers.ReadOnlyField(source='category.id')
