from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    national_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_lenght=20)
    address = models.CharField(max_length=500)
