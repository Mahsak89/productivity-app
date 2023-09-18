from rest_framework import generics, permissions
from productivity_app.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer


class TaskList(generics.ListCreateAPIView):
    """
    List Tasks or create a task if logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()
