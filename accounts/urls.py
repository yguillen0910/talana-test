from django.urls import path
from rest_framework import routers
from . import views
from accounts.api.login import Login


urlpatterns = [
    path('api/login/', Login.as_view(), name='login'),
]
