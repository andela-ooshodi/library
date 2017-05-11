from rest_framework import mixins, viewsets

from bookshelf.models import Category, Book

from .serializers import CategorySerializer, BookSerializer


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

