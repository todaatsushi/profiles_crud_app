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


# class BaseUserUpdateForm(auth_forms.UserChangeForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

#     class Meta(auth_forms.UserChangeForm):
#         model = BaseUser
#         fields = [
#             'email', 'first_name', 'last_name',
#             'about', 'company', 'role', 'responsibilities'
#         ]

#     def clean(self):
#         """
#         Make sure password and confirm password are matching.
#         """
#         cleaned = super().clean()
#         password = cleaned.get('password')
#         confirm = cleaned.get('confirm_password')

#         if password != confirm:
#             raise forms.ValidationError(
#                 "Your passwords don't match! Please enter them again."
#             )

#         return cleaned
