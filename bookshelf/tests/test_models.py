from django.test import TestCase

from bookshelf.models import Category, Book


class BookAppModelsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Space',
            description='This is a book about space'
        )
        self.book = Book.objects.create(
            name='Space voyage',
            description='The journey of captain rogers',
            author='Captain Rogers',
            category=self.category
        )

    def tearDown(self):
        Category.objects.all().delete()
        Book.objects.all().delete()

    def test_get_category_from_db(self):
        category = Category.objects.get(name='Space')
        self.assertTrue(hasattr(category, '__str__'))
        # check if the __str__ method of category would print out it's name
        self.assertEqual(category.__str__(), 'Space')
        self.assertEqual(category.name, 'Space')
        self.assertEqual(category.description, 'This is a book about space')

    def test_get_book_from_db(self):
        book = Book.objects.get(name='Space voyage')
        self.assertTrue(hasattr(book, '__str__'))
        # check if the __str__ method of book would print out it's name
        self.assertEqual(book.__str__(), 'Space voyage')
        self.assertEqual(book.name, 'Space voyage')
        self.assertEqual(book.description, 'The journey of captain rogers')
        self.assertEqual(book.author, 'Captain Rogers')
        self.assertEqual(book.category, self.category)
