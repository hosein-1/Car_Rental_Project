from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Car
from .forms import ReservationForm


def cars_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'cars/cars_list.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    form = ReservationForm()
    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car_detail.html', context)




