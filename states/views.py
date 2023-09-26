from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from productivity_app.permissions import IsOwnerOrReadOnly
from states.models import State
from states.serializers import StateSerializer


class StateList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StateSerializer
    queryset = State.objects.all()

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


class StateDetail(generics.RetrieveDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StateSerializer
    queryset = State.objects.all()
