from django.contrib import admin

from products.models import Brand
from products.models import Car
from products.models import CarModel
from products.models import Reservation

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(Reservation)
