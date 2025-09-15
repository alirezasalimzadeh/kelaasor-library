from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='Phone Number')

    def __str__(self):
        return self.get_full_name()
