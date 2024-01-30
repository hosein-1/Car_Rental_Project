from django.urls import path

from . import views


urlpatterns = [
    path('questions/', views.ask_question, name='ask_question'),
    path('about-us/', views.about_us_view, name='about_us'),
]