from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
from productivity_app.permissions import IsOwnerOrReadOnly


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = Category.objects.all()

    filter_backends = [
        DjangoFilterBackend,  # Use Django filters

    ]
    filterset_fields = [
        'owner',
        'owner__id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
