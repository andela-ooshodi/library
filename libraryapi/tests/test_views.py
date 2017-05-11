from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from bookshelf.models import Category, Book


class LibraryApiViewTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Space',
            description='All about space'
        )
        self.book = Book.objects.create(
            name='Space Voyage',
            description='The journey of captain rogers',
            author='Captain Rogers',
            category=self.category
        )

    def test_can_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
