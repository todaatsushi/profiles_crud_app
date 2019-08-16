import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.urls import reverse
# Provides mandatory methods to use for admin
from django.contrib.auth.models import PermissionsMixin

from users.managers import CustomBaseUserManager


def generate_id():
    """
    Generate unique user ids.
    """
    return uuid.uuid4().hex


class BaseUser(AbstractBaseUser, PermissionsMixin):
    id = models.TextField(
        primary_key=True,
        default=generate_id
    )

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    # User status
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # User profile fields
    # Personal
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    about = models.TextField()

    # Job details
    company = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    responsibilities = models.TextField(null=True)

    objects = CustomBaseUserManager()

    # Settings
    USERNAME_FIELD = 'email'

    def __str__(self):
        return '{} - {}'.format(self.email, self.id)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})
