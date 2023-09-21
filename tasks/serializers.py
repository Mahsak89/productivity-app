from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'category',
            'title', 'description', 'created_at', 'updated_at', 'startdate',
            'deadline', 'priority', 'state'
        ]


class TaskDetailSerializer(TaskSerializer):

    category = serializers.ReadOnlyField(source='category.id')
