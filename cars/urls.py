from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars_list, name='cars_list'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
    path('profile/', views.user_profile, name='profile'),
    path('search/', views.search, name='search_cars'),
    path('payment/', views.payment, name='payment'),
]