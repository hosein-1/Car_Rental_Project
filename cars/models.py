from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=500)
    number_plate = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'ماشین'

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work_experience = models.CharField(max_length=255)
    certificate_base = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Reservation(models.Model):
    PAID = 'p'
    UNPAID = 'up'
    PAYMENT_STATUS = [
        (PAID, 'paid'),
        (UNPAID, 'unpaid')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, blank=True)
    start_date = jmodels.jDateTimeField(auto_now_add=True)
    end_date = jmodels.jDateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=500)
    is_paid = models.CharField(max_length=6, choices=PAYMENT_STATUS, default=PAID)

    def __str__(self):
        return f'{self.customer} : {self.car}'
