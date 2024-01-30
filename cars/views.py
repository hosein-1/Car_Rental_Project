from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Car, Customer
from .forms import ReservationForm


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


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserve_object = form.save(commit=False)
            reserve_object.customer = customer
            reserve_object.car = car
            reserve_object.is_paid = 'p'
            form.save()
            return redirect('cars_list')
    else:
        form = ReservationForm()

    context = {
        'car': car,
        'form': form,
    }
    return render(request, 'cars/car_detail.html', context)


# @require_POST
# def reserve_car(request):
#     form = ReservationForm(request.POST)
#     if form.is_valid():
#


