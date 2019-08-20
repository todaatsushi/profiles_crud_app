"""
Custom mixins based on UserPassesTestMixin.
"""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model


class IsOwnerOrStaffTestMixin(UserPassesTestMixin):
    """
    Only allows users to delete/update profiles if it belongs to them or
    if they are a staff member.
    """
    def test_func(self):
        profile = self.get_object()

        # True if the request user is the owner of the profile
        # and True if user is staff. Else return False.
        return self.request.user == profile or self.request.user.is_staff


class IsLoggedOutTestMixin(UserPassesTestMixin):
    """
    Only allows users to create profiles if they are logged out.
    """
    def test_func(self):
        User = get_user_model()
        all_users = User.objects.all()

        return False if self.request.user in all_users else True
