from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=500)
    number_plate = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work_experience = models.CharField(max_length=255)
    certificate_base = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.driver.first_name} {self.driver.last_name}'

