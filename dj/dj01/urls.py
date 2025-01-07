from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # Главная страница
    path("data", views.data),  # Страница "data"
    path("test", views.test),  # Страница "test"
]
