from rest_framework import serializers

from bookshelf.models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )

    class Meta:
        model = Category
        fields = ('name', 'description', 'books')


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'description', 'author', 'category')
