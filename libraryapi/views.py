from rest_framework import mixins, viewsets

from bookshelf.models import Category, Book

from .serializers import CategorySerializer, BookSerializer


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Optionally retrieve/list categories by its name
        """
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Optionally retrieve/list books by its name
        """
        queryset = Book.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

