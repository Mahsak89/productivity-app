from django.db import IntegrityError
from rest_framework import serializers
from states.models import State


class StateSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = State
        fields = ['id', 'created_at', 'owner', 'task']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
