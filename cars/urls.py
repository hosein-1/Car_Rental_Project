from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars_list, name='cars_list'),
]