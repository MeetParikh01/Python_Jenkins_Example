"""
models for users app
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
# Create your models here.


class User(AbstractUser):
    """
    User Model
    """
    contact = PhoneField(blank=True, null=True)
