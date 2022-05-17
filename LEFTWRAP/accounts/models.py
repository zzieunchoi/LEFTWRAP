from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    division = models.BooleanField(default=False)
    leftwrap = models.BooleanField(default=False)