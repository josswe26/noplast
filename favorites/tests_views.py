from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product


# Create your tests here.
class TestFavoritesViews(TestCase):
    """Test the favorites view"""

    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user',
                                                  password='test_password')
        self.client.login(username='test_user', password='test_password')

    def test_get_favorites_page(self):
        """ Test the favorites page is displayed """
        response = self.client.get('/favorites/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/favorites.html')
        self.assertEqual(self.test_user.favorite_products.count(), 0)
