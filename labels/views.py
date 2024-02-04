from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Label
from .serializers import LabelSerializer
from productivity_app.permissions import IsOwnerOrReadOnly


class LabelList(generics.ListCreateAPIView):
    serializer_class = LabelSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Label.objects.all()

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters

    ]
    filterset_fields = [
        'owner',
        'owner__id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
