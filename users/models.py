from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=50)
    about = models.TextField()
    image = models.ImageField(
        default='default_profile.jpg',
        upload_to='profile_pics'
    )

    company = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='Tour Guide')
    skills = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        dims = (200, 200)

        if img.height > 200 or img.width > 200:
            img.thumbnail(dims)
            img.save(self.image.path)

