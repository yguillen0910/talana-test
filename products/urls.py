from django.urls import path
from rest_framework import routers
from . import views
from products.api.car import CarsAvailableAPI 


urlpatterns = [
    path('api/cars/', CarsAvailableAPI.as_view(), name='cars'),
]
