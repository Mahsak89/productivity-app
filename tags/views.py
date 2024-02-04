from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tag
from .serializers import TagSerializer
from productivity_app.permissions import IsOwnerOrReadOnly


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Tag.objects.all()

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters

    ]
    filterset_fields = [
        'owner',
        'owner__id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
