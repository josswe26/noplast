from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestReviewsViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user',
                                                  password='test_password')
        self.client.login(username='test_user', password='test_password')


    def test_get_reviews_page(self):
        """ Test the reviews page is displayed """
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')


