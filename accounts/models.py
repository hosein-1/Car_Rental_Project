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
    email = models.EmailField(verbose_name='آدرس ایمیل', unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=255)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=255)
    national_code = models.CharField(verbose_name='کد ملی', max_length=20)
    phone_number = models.CharField(verbose_name='شماره تلفن', max_length=20)
    address = models.CharField(max_length=500)
    age = models.PositiveIntegerField(verbose_name='سن', blank=True, null=True)



