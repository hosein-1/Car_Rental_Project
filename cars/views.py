from django.shortcuts import render, HttpResponse

from .models import Car


def cars_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'cars/cars_list.html', context)


