from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # phone = models.CharField(max_length=15, blank=True, null=False)
    profile = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def fullname(self):
        return self.get_full_name()