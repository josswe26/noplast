from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import Review

# Create your tests here.
class TestReviewsViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user',
                                                  password='test_password')
        self.test_product = Product.objects.create(name='test_product',
                                                   description='Test product',
                                                   price=10)
        self.client.login(username='test_user', password='test_password')


    def test_get_reviews_page(self):
        """ Test the reviews page is displayed """
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')


    def test_get_add_review_page(self):
        """ Test the add review page is displayed """
        response = self.client.get(f'/reviews/add_review/{self.test_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')


    def test_add_review(self):
        """ Test a review is added to the product """
        self.client.post(f'/reviews/add_review/{self.test_product.id}/', {
            'title': 'Test title',
            'content': 'Test content',
            'rating': 5,
        })
        review = Review.objects.filter(title='Test title')
        self.assertEqual(len(review), 1)
