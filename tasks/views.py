from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from productivity_app.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List Tasks or create a task if logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.annotate(
        states_count=Count('states', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'states__owner__profile',
        'owner__profile',
        'category',
        'priority',
        'deadline',
        'created_at',
        'startdate',



    ]
    search_fields = [
        'category__name',
    ]
    ordering_fields = [
        'priority',
        'deadline',
        'created_at',
        'category',
        'startdate',
        'states_count',
        'states__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.annotate(
        states_count=Count('states', distinct=True)
    ).order_by('-created_at')
