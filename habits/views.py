from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from productivity_app.permissions import IsOwnerOrReadOnly

from .models import Habit
from .serializers import HabitSerializer
from datetime import date


class HabitList(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'owner',
    ]

    ordering_fields = [
        'created_at',
    ]


class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Habit.objects.all()
