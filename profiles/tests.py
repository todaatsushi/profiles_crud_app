from django.test import TestCase
from django.urls import reverse


class BasicViewsTestCase(TestCase):
    def test_home_view_redirects(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_base_user_login_serves_template(self):
        response = self.client.get(reverse('user-login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_login.html')

