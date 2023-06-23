from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    artistic_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "This field must be unique."
        }
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists."
        }
    )
