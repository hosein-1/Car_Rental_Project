from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CUSTOMER = 'c'
    DRIVER = 'd'
    ADMIN = 'a'
    USER_STATUS = [
        (CUSTOMER, 'customer'),
        (DRIVER, 'driver'),
        (ADMIN, 'admin')
    ]
    national_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    age = models.PositiveIntegerField(default=None)
    user_type = models.CharField(max_length=1, choices=USER_STATUS, default=CUSTOMER)


