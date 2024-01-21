from django.db import models
from django.conf import settings


class Customer(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=500)
    number_plate = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=True)
