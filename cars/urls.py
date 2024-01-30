from django.urls import path

from . import views


urlpatterns = [
    path('cars/', views.cars_list, name='cars_list'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
]