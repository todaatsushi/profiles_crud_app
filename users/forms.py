from django import forms
import django.contrib.auth.forms as auth_forms

from users.models import BaseUser


# Registration/Update Form
class BaseUserCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm):
        model = BaseUser
        fields = [
            'email', 'first_name', 'last_name',
            'about', 'company', 'role', 'responsibilities'
        ]


class BaseUserUpdateForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm):
        model = BaseUser
        fields = [
            'email', 'first_name', 'last_name',
            'about', 'company', 'role', 'responsibilities'
        ]
