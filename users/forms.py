from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import BaseUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = BaseUser
        fields = (
            'email', 'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = BaseUser
        fields = (
            'email', 'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )
