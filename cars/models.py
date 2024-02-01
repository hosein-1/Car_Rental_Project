from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels
from datetime import timedelta, datetime


class Category(models.Model):
    name = models.CharField(max_length=255)

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
    car_image = models.ImageField(upload_to='cars/cars_image/', default='cars/cars_image/default.png')
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'ماشین'

    def __str__(self):
        return f'{self.name}'


class Reservation(models.Model):
    PAID = 'p'
    UNPAID = 'up'
    PAYMENT_STATUS = [
        (PAID, 'پرداخت شده'),
        (UNPAID, 'پرداخت نشده')
    ]

    WITH_DRIVER = 'wd'
    WITHOUT_DRIVER = 'wod'

    DRIVER_STATUS = [
        (WITH_DRIVER, 'با راننده'),
        (WITHOUT_DRIVER, 'بدون راننده'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    driver = models.CharField(verbose_name='راننده', max_length=3, choices=DRIVER_STATUS, default=WITH_DRIVER)
    start_date = jmodels.jDateField(verbose_name='تاریخ شروع', default=datetime.today())
    end_date = jmodels.jDateField(verbose_name='تاریخ پایان', default=datetime.today() + timedelta(days=2))
    delivery_address = models.CharField(verbose_name='آدرس محل تحویل', max_length=500)
    is_paid = models.CharField(max_length=6, choices=PAYMENT_STATUS, default=UNPAID)

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو'

    def __str__(self):
        return f'{self.user} : {self.car}'
