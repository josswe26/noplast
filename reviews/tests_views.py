from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .views import update_product_rating


# Create your tests here.
class TestReviewsViews(TestCase):
    """ Test for the Review app views """
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user',
                                                  password='test_password')
        self.test_product = Product.objects.create(name='test_product',
                                                   description='Test product',
                                                   price=10,
                                                   rating=None)
        self.client.login(username='test_user', password='test_password')

    # Tests for page rendering

    def test_get_reviews_page(self):
        """ Test the reviews page is displayed """
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_get_add_review_page(self):
        """ Test the add review page is displayed """
        response = self.client.get(
            f'/reviews/add_review/{self.test_product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_get_edit_review_page(self):
        """ Test the edit review page is displayed """
        test_review = Review.objects.create(author=self.test_user,
                                            product=self.test_product,
                                            title='Test review',
                                            content='Test content',
                                            rating=5)
        response = self.client.get(f'/reviews/edit_review/{test_review.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    # Tests for page functionality

    def test_add_review(self):
        """ Test a review is added to the product """
        # Attempt to add a review
        self.client.post(f'/reviews/add_review/{self.test_product.id}/', {
            'title': 'Test title',
            'content': 'Test content',
            'rating': 5,
        })
        review = Review.objects.filter(title='Test title')
        self.assertEqual(len(review), 1)
        # Attempt to submit a second review
        response = self.client.post(
            f'/reviews/add_review/{self.test_product.id}/', {
                'title': 'Test title 2',
                'content': 'Test content 2',
                'rating': 5,
            })
        all_reviews = Review.objects.all()
        # Check the user can only submit one review per product
        self.assertEqual(len(all_reviews), 1)
        self.assertRedirects(response, f'/products/{self.test_product.id}/')

    def test_edit_review(self):
        """ Test a review can be edited """
        # Create test review
        test_review = Review.objects.create(author=self.test_user,
                                            product=self.test_product,
                                            title='Test review',
                                            content='Test content',
                                            rating=5)
        # Submit form to edit review with altered content
        response = self.client.post(f'/reviews/edit_review/{test_review.id}/', {
            'title': test_review.title,
            'content': 'Edited content',
            'rating': test_review.rating,
        })
        self.assertRedirects(response, f'/products/{test_review.product.id}/')
        self.assertEqual(Review.objects.last().content, "Edited content")


    def test_update_product_rating(self):
        """ Test the product rating is being updated """
        self.client.post(f'/reviews/add_review/{self.test_product.id}/', {
            'title': 'Test title',
            'content': 'Test content',
            'rating': 4,
        })
        update_product_rating(self.test_product)
        self.assertEqual(self.test_product.rating, 4)
        self.client.logout()
        # Test average with second product rating
        self.test_user2 = User.objects.create_user(username='test_user2',
                                                   password='test_password2')
        self.client.login(username='test_user2', password='test_password2')
        self.client.post(f'/reviews/add_review/{self.test_product.id}/', {
            'title': 'Test title',
            'content': 'Test content',
            'rating': 2,
        })
        update_product_rating(self.test_product)
        self.assertEqual(self.test_product.rating, 3)
