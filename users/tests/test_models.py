from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagerTestCase(TestCase):
    def test_create_user(self):
        """
        Using the custom UserManager, test if we can create a normal user with valid credentials.
        """
        # Create user
        User = get_user_model()
        user = User.objects.create_user(email='test@mail.com', password='test')

        self.assertEqual(user.email, 'test@mail.com')
        self.assertFalse(user.is_superuser)

        ## Custom User has no username
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        # No args
        with self.assertRaises(ValueError):
            User.objects.create_user()

        # invalid email, no password
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')

        # invalid email only
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='valid')

    def test_create_superuser(self):
        """
        Using the custom UserManager, test if we can create a staff user with valid credentials.
        """
        # Create user
        User = get_user_model()
        staff = User.objects.create_superuser(email='test@mail.com', password='test')

        self.assertEqual(staff.email, 'test@mail.com')
        self.assertTrue(staff.is_superuser)

        ## Custom User has no username
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        # Check method with invalid args
        # No args
        with self.assertRaises(ValueError):
            User.objects.create_superuser()

        # invalid email, no password
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='')

        # invalid email only
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='', password='valid')

