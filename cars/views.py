from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.decorators.http import require_POST


from .models import Car, Reservation, Category
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
def car_reserve(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reserve_object = form.save(commit=False)
            reserve_object.user = request.user
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
    return render(request, 'cars/car_reserve.html', context)


@login_required()
def payment(request):
    reserve_object = Reservation.objects.filter(user_id=request.user.id).filter(is_paid='up').last()
    if reserve_object:
        total_price = (reserve_object.end_date.day - reserve_object.start_date.day) * reserve_object.car.price

    else:
        total_price = 0

    if request.method == 'POST':
        reserve_object.is_paid = 'p'
        reserve_object.save()
        return redirect('profile')

    context = {
        'reserve_object': reserve_object,
        'total_price': total_price,
    }
    return render(request, 'cars/payment.html', context)


@login_required()
def user_profile(request):
    cars_reserve = Reservation.objects.filter(user_id=request.user.id)

    context = {
        'cars_reserve': cars_reserve,
        'banner': False
    }

    return render(request, 'profile.html', context)


def search(request):
    search_query = request.GET.get('q')
    category_query = request.GET.get('category')
    
    search_list = Car.objects.all()

    if category_query and category_query != '-1':
        search_list = search_list.filter(category_id=category_query)

    if search_query:
        search_list = search_list.filter(
            Q(name__icontains=search_query) | Q(category__name__icontains=search_query) | Q(model__icontains=search_query)
        )

    paginator = Paginator(search_list, 12)
    page_number = request.GET.get('page', 1)
    try:
        object_list = paginator.page(page_number)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        object_list = paginator.page(1)

    context = {
        'query': search_query,
        'category_selected': int(category_query),
        'categories': Category.objects.all(),
        'object_list': object_list,
        'pages': object_list,
        'banner': False,
        'last_page': max(object_list.paginator.page_range),
        'pagens': range(object_list.number - 4, object_list.number + 5),

    }

    return render(request, 'cars/search_list.html', context)


