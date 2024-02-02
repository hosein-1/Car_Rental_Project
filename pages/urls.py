from django.urls import path

from . import views


urlpatterns = [
    path('p/<str:slug>', views.page, name='page'),
    path('questions/ask', views.ask_question, name='ask_question'),
    path('questions/<int:id>', views.question, name='question'),
    path('questions/', views.questions_list, name='questions_list'),
]