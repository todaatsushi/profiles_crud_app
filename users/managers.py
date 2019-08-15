from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q


class CustomBaseUserManager(BaseUserManager):
    """
    Custom user model manager. No username field,
    """
    def create_user(self, email, password, **kwargs):
        """
        Create and then save base user instances given at least the email and password.
        """
        # Check args
        if not email:
            raise ValueError('Email must not be empty.')
        if not password:
            raise ValueError('Password must not be empty.')

        # Formatting args
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Create and then save staff/super user instances given at least the email and password.
        """
        # If blank, set to True
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must be have is_superuser = True')

        return self.create_user(email, password, **kwargs)


    def get_by_email(self, email):
        """
        Be able to search for a user by the unique email.
        """
        return self.filter(Q(email=email))
