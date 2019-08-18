from django.test import TestCase
from django.contrib.auth import get_user_model

import users.forms as forms


class BaseUserCreateFormTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'wilfred',
            'email': 'wilfred@mail.com',
            'first_name': 'Wilfred',
            'last_name': 'Ndidi',
            'about': 'Ball winning midfielder for LFC',
            'company': 'Leicester FC',
            'role': 'Holding Midfielder',
            'responsibilities': 'Win back possession of the ball',
            'password1': 'testing321',
            'password2': 'testing321'
        }

        self.invalid_data = {
            'username': 'wilfred',
            'email': 'wilfred@mail.com',
            'first_name': 'Wilfred',
            'last_name': 'Ndidi',
            'about': 'Ball winning midfielder for LFC',
            'company': 'Leicester FC',
            'role': 'Holding Midfielder',
            'responsibilities': 'Win back possession of the ball',
            'password1': 'invalid',
            'password2': 'invalid'
        }

    def test_form_can_validate_data(self):
        valid_form = forms.BaseUserCreateForm(data=self.valid_data)
        self.assertTrue(valid_form.is_valid())

        invalid_form = forms.BaseUserCreateForm(data=self.invalid_data)
        self.assertFalse(invalid_form.is_valid())


class BaseUserUpdateFormTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
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

    def test_form_can_validate_data(self):
        """
        Test that BaseUserUpdateForm can detect both valid
        and invalid data from BaseUser instances.
        """
        pass
