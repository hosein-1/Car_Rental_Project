from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'model', 'color', 'price']


@admin.register(models.Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ['user', 'car', 'driver', 'is_paid']
