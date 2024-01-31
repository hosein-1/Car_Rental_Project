from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages


from .models import Car, Customer, Reservation
from .forms import ReservationForm


def home(request):
    cars = Car.objects.all()[:6]
    context = {
        'cars': cars,
    }
    return render(request, 'cars/home.html', context)


def cars_list(request):
    cars = Car.objects.all()

    paginator = Paginator(cars, 12)
    page_number = request.GET.get('page', 1)
    try:
        cars = paginator.page(page_number)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        cars = paginator.page(1)

    context = {
        'cars': cars,
        'page': cars,
        'last_page': max(cars.paginator.page_range),
        'pagens': range(cars.number -4 , cars.number + 5),
    }
    return render(request, 'cars/cars_list.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    context = {
        'car': car,
        'banner': False
    }
    return render(request, 'cars/car_detail.html', context)



@login_required()
def car_reserv(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == 'POST':
        try:
            customer = Customer.objects.get(user=request.user)
        except:
            messages.warning(request, 'لطفا با سطح دسترسی کاربر معمولی وارد شوید.')
            return render(request, 'cars/home.html')

        form = ReservationForm(request.POST)
        if form.is_valid():
            reserve_object = form.save(commit=False)
            reserve_object.customer = customer
            reserve_object.car = car
            form.save()
            return redirect('payment')
    else:
        form = ReservationForm()

    context = {
        'car': car,
        'form': form,
        'banner': False
    }
    return render(request, 'cars/car_reserv.html', context)


@login_required()
def payment(request):
    reserve_object = Reservation.objects.filter(customer__user_id=request.user.id).filter(is_paid='up').first()
    total_price = (reserve_object.end_date.day - reserve_object.start_date.day) * reserve_object.car.car_price

    if request.method == 'POST':
        reserve_object.is_paid = 'p'
        return redirect('profile')

    context = {
        'reserve_object': reserve_object,
        'total_price': total_price,
    }
    return render(request, 'cars/payment.html', context)


@login_required()
def user_profile(request):
    cars_reserve = Reservation.objects.filter(customer__user_id=request.user.id)

    context = {
        'cars_reserve': cars_reserve,
        'banner': False
    }

    return render(request, 'profile.html', context)


def search(request):
    query = request.GET.get('q')

    if query:
        object_list = Car.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query) | Q(model__icontains=query)
        )
    else:
        object_list = None

    context = {
        'query': query,
        'object_list': object_list,
        'banner': False,
    }
    return render(request, 'cars/search_list.html', context)
