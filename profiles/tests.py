from django.test import TestCase, tag
from django.urls import reverse


class BasicViewsTestCase(TestCase):
    """
    Test all views serve templates in the urls at the top level
    of the app:
    - Home
    """

    @tag('unit')
    def test_home_view_redirects(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)