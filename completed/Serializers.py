from rest_framework import serializers
from completed.models import Complete


class CompleteSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Complete
        fields = ['id', 'created_at', 'owner', 'task']
