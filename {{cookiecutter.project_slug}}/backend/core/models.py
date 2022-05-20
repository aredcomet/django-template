from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = 'Users'
        ordering = [
            "-id",
        ]

    def __str__(self) -> str:
        return self.username
