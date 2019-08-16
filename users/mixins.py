"""
Custom mixins based on UserPassesTestMixin.
"""
from django.contrib.auth.mixins import UserPassesTestMixin


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
        return False if self.request.user else True