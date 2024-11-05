from django.db import models
from django.contrib.auth.models import AbstractUser as BaseAbstractUser

class User(BaseAbstractUser):
    email = models.EmailField(unique=True)