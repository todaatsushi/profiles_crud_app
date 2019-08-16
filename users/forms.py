from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import BaseUser


# Admin forms
class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = BaseUser
        fields = (
            'email', 'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )


class BaseUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = BaseUser
        fields = (
            'email', 'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )


# User forms
# class BaseUserRegisterForm():
#     pass