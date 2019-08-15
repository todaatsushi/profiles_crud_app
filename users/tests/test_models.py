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
        with self.assertRaises(TypeError):
            User.objects.create_user()

        # invalid email, no password
        with self.assertRaises(TypeError):
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
        staff = User.objects.create_superuser(
            email='test@mail.com', password='test', is_superuser=True
        )

        self.assertEqual(staff.email, 'test@mail.com')
        self.assertTrue(staff.is_superuser)

        ## Custom User has no username
        try:
            self.assertIsNone(staff.username)
        except AttributeError:
            pass

        # test that superuser cannot be created with is_superuser = False
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='test@mail.com',
                password='test',
                is_superuser=False
            )

    def test_get_by_email(self):
        """
        Test manager class's filter method - get_by_email
        """
        # Create user
        User = get_user_model()
        user = User.objects.create_user(email='test@mail.com', password='test')

        query = User.objects.get_by_email('test@mail.com').first()
        self.assertEqual(user, query)

