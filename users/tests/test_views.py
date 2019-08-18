from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UsersViewsTestCase(TestCase):
    """
    Unit tests for all the views in the users app.

    Each view will have tests to see if they can sucessfully serve
    templates required.

    Views with authentication/test functions will have them tested
    also.
    """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='jane@mail.com',
            username='jane',
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
            username='john',
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
            username='janet',
            first_name='Janet',
            last_name='Doel',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None',

            is_staff=True,
            is_superuser=True
        )

    # Profile management
    def test_base_users_list_view_serves_template(self):
        response = self.client.get(reverse('user-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_list.html')

    def test_base_user_detail_view_serves_template(self):
        response = self.client.get(reverse('user-detail', kwargs={
            'slug': self.user.username
        }))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_detail.html')

    def test_base_user_create_view_authentication_works(self):
        """
        Test if create view only allows non logged in user
        to access.
        """
        # Not logged in
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

        # Logged in
        self.client.force_login(self.user)
        forbidden_response = self.client.get(reverse('user-create'))
        self.assertEqual(forbidden_response.status_code, 403)

    def test_base_user_create_view_serves_template(self):
        response = self.client.get(reverse('user-create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_create.html')

    def test_base_user_update_view_authentication_for_regular_users_work(self):
        """
        Test if users can only update their own profiles.
        """
        # Not logged in
        not_logged_in_response = self.client.get(
            reverse('user-update', kwargs={'slug': self.user.username})
        )
        # Redirect to login
        self.assertEqual(not_logged_in_response.status_code, 302)

        # Not own profile
        self.client.force_login(self.user)
        other_user_response = self.client.get(
            reverse('user-update', kwargs={'slug': self.user2.username})
        )
        self.assertEqual(other_user_response.status_code, 403)
        
        # Own profile
        same_user_response = self.client.get(
            reverse('user-update', kwargs={'slug': self.user.username})
        )
        self.assertEqual(same_user_response.status_code, 200)
    
    def test_base_user_update_view_authentication_for_staff_users_work(self):
        """
        Test staff users can update any user's profile.
        """
        self.client.force_login(self.staff)

        staff_own_profile_response = self.client.get(
            reverse('user-update', kwargs={'slug': self.staff.username})
        )
        self.assertEqual(staff_own_profile_response.status_code, 200)

        regular_user_profile_response = self.client.get(
            reverse('user-update', kwargs={'slug': self.user.username})
        )
        self.assertEqual(regular_user_profile_response.status_code, 200)

    def test_base_user_update_view_serves_template(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('user-update', kwargs={'slug': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_update.html')

    def test_base_user_delete_view_authentication_for_regular_users_work(self):
        """
        Test if users can only delete their own profiles.
        """
        # Not logged in
        not_logged_in_response = self.client.get(
            reverse('user-delete', kwargs={'slug': self.user.username})
        )
        # Redirect to login
        self.assertEqual(not_logged_in_response.status_code, 302)

        # Not own profile
        self.client.force_login(self.user)
        other_user_response = self.client.get(
            reverse('user-delete', kwargs={'slug': self.user2.username})
        )
        self.assertEqual(other_user_response.status_code, 403)
        
        # Own profile
        same_user_response = self.client.get(
            reverse('user-delete', kwargs={'slug': self.user.username})
        )
        self.assertEqual(same_user_response.status_code, 200)
    
    def test_base_user_delete_view_authentication_for_staff_users_work(self):
        """
        Test staff users can delete any user's profile.
        """
        self.client.force_login(self.staff)

        staff_own_profile_response = self.client.get(
            reverse('user-delete', kwargs={'slug': self.staff.username})
        )
        self.assertEqual(staff_own_profile_response.status_code, 200)

        regular_user_profile_response = self.client.get(
            reverse('user-delete', kwargs={'slug': self.user.username})
        )
        self.assertEqual(regular_user_profile_response.status_code, 200)

    # Login/Password management tests
    def test_base_user_login_serves_template(self):
        response = self.client.get(reverse('user-login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_login.html')

    def test_base_user_reset_password_serves_template(self):
        # Make user to reset password
        User = get_user_model()
        user = User.objects.create_user(
            email='test@mail.com',
            password='foo',
            username='John'
        )

        # login new user
        self.client.force_login(user)
        response = self.client.get(reverse('password-change'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/user_password_change.html')

    def test_base_user_reset_password_authentication(self):
        response = self.client.get(reverse('password-change'))
        self.assertEqual(response.status_code, 302)

