from django.contrib import admin

from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'model', 'color', 'price']