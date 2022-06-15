from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.TextField(max_length=40)
    last_name = models.TextField(max_length=40)