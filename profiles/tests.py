from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class BasicViewsTestCase(TestCase):
    """
    Test all views serve templates in the urls at the top level
    of the app:
    - Home
    """
    def test_home_view_redirects(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)