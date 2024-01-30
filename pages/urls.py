from django.urls import path

from . import views


urlpatterns = [
    path('questions/', views.ask_question, name='ask_question'),
]