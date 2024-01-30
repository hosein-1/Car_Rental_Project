from django.shortcuts import render, HttpResponse

from .models import Car


def home(request):
    cars = Car.objects.all()[:6]
    context = {
        'cars': cars,
    }
    return render(request, 'cars/home.html', context)



def cars_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'cars/cars_list.html', context)


