from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from productivity_app.permissions import IsOwnerOrReadOnly

from .models import HabitCompletion
from .serializers import HabitCompletionSerializer
from datetime import date


class HabitCompletionList(generics.ListCreateAPIView):
    serializer_class = HabitCompletionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = HabitCompletion.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'owner',
        'Habit',
    ]


class HabitCompletionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitCompletionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = HabitCompletion.objects.all()
