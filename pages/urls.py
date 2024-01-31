from django.urls import path

from . import views


urlpatterns = [
    path('p/<str:slug>', views.page, name='page'),
    path('questions/', views.ask_question, name='ask_question'),
]