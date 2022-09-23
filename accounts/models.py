from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True, verbose_name="Picture of account")
    birthday = models.DateField("Date of birth", null=True)
    phone = models.CharField("Phone number", max_length=14, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.username)
