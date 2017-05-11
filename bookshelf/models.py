from __future__ import unicode_literals

from django.db import models


class Base(models.Model):
    """
    Base model
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True, default='No description')

    class Meta:
        abstract = True

    def __str__(self):
        """
        :return: string representation of the object
        """
        return self.name


class Category(Base):
    pass


class Book(Base):
    author = models.CharField(max_length=50, default='Unknown')
    category = models.ForeignKey(Category, related_name='books')
