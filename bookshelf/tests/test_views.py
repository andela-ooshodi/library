from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from bookshelf.models import Category, Book

# Create your tests here.


class InventoryViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
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

    def tearDown(self):
        Category.objects.all().delete()
        Book.objects.all().delete()

    def test_can_reach_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'bookshelf/base.html')

    def test_can_reach_404_page(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'bookshelf/404.html')

    def test_can_search(self):
        query_data = {
            'name': 'space'
        }
        response = self.client.get(reverse('result'), query_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Space', response.content)
        self.assertIn('Space Voyage', response.content)
        self.assertIn('Captain Rogers', response.content)

    def test_no_result(self):
        query_data = {
            'name': 'Not found'
        }
        response = self.client.get(reverse('result'), query_data)
        # redirect to 404 page
        self.assertEqual(response.status_code, 302)

    def test_empty_query(self):
        # Navigating to the result page without any query parameters
        response = self.client.get(reverse('result'))
        # redirect to 404 page
        self.assertEqual(response.status_code, 302)
