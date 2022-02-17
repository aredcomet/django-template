from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.username
