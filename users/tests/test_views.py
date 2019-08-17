from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UsersViewsTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='jane@mail.com',
            password='foo',
            first_name='Jane',
            last_name='Doe',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None'
        )

        self.user2 = User.objects.create_user(
            email='john@mail.com',
            password='foo',
            first_name='John',
            last_name='Doe',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None'
        )

        self.staff = User.objects.create_superuser(
            email='staff@mail.com',
            password='foo',
            first_name='Janet',
            last_name='Doel',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None',

            is_staff=True,
            is_superuser=True
        )

    def test_all_base_users_view_template(self):
        response = self.client.get(reverse('user-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_list.html')

    def test_base_user_detail_view_template(self):
        response = self.client.get(reverse('user-detail', kwargs={
            'pk': self.user.pk
        }))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_detail.html')

    def test_base_user_create_view_authentication(self):
        """
        Test if create view only allows non logged in user
        to access.
        """
        # Not logged in
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

        # Logged in
        self.client.force_login(self.user)
        forbidden = self.client.get(reverse('user-create'))
        self.assertEqual(forbidden.status_code, 403)

    def test_base_user_create_view_template(self):
        response = self.client.get(reverse('user-create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_create')
        pass

    def test_base_user_update_view_authentication(self):
        pass

    def test_base_user_update_view_template(self):
        pass
    
    def test_base_user_delete_view_authentication(self):
        pass

    def test_base_user_delete_view_template(self):
        pass
