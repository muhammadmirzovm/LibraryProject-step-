from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author , Category, Book
from django.contrib.auth.models import User
class AuthorAPITest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Test Author",
            bio = 'This is a bio that is longer than twenty characters'
        )
        self.user = User.objects.create_user(username='admin1', password='admin1234')

    def test_get_authors_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author_without_auth(self):
        data = {'name': 'New Author', 'bio': 'This bio is definitely longer than twenty characters'}
        response = self.client.post('/api/authors/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_author_with_auth(self):
        self.client.login(username='admin1', password='admin1234')
        data = {'name': 'New Author', 'bio': 'This bio is definitely longer than twenty characters'}
        response = self.client.post('/api/authors/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_author_invalid_bio(self):
        self.client.login(username='admin1', password='admin1234')
        data = {'name':'New author', 'bio':'Thisbiolessthan20'}
        response = self.client.post('/api/authors/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class BookAPITest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="James Clear",
            bio = "This is a bio that is longer than twenty characters"
        )
        self.book = Book.objects.create(
            title = "Atomic Habits",
            description = 'Tiny changes remarkable results', 
            published_date = "2026-01-01",
            price = '300.30',
            author = self.author)
        self.book2 = Book.objects.create(
            title = "Mountain",
            description = 'Big success does not came without big risk and many mistakes', 
            published_date = "2022-02-02",
            price = '500.30',
            author = self.author)
        
            
    def test_get_books_list(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_search_books(self):
        response = self.client.get("/api/books/?search=Atomic")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        
    def test_filter_by_author(self):
        response = self.client.get(f"/api/books/?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_ordering_by_price(self):
        response = self.client.get("/api/books/?ordering=price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][1]['title'], 'Mountain')
        