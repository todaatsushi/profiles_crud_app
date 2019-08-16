from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import BaseUser

# Admin
class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = BaseUser
        fields = (
            'email', 'password',
            'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )


class BaseUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = BaseUser
        fields = (
            'email', 'password',
            'first_name', 'last_name',
            'about', 'company', 'role',
            'responsibilities',
        )


# Registration/Update Form
class BaseUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = BaseUser
        fields = [
            'email', 'first_name', 'last_name',
            'about', 'company', 'role', 'responsibilities'
        ]

    def clean(self):
        cleaned = super().clean()
        password = cleaned.get('password')
        confirm = cleaned.get('confirm_password')

        if password != confirm:
            raise forms.ValidationError(
                "Your passwords don't match! Please enter them again."
            )
