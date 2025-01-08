from django.urls import path
from . import views

urlpatterns = [
    path("", views.data, name="dj02_home"),  # перенаправление на data для dj02/
    path("data", views.data, name="data"),
    path("data_2", views.data_2, name="data_2"),
    path("data_3", views.data_3, name="data_3"),
    path("test", views.test, name="test"),
]
