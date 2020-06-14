from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import OneToOneField
from django.db.models import IntegerField
from django.db.models import BooleanField
from django.db.models import ForeignKey
from django.db.models import ImageField
from django.db.models import CASCADE
from accounts.models import Profile

class Brand(Model):

    name = CharField(
        max_length=200,
        null=False,
        blank=False
    )

    created = DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated = DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

class CarModel(Model):
    
    name = CharField(
        max_length=200,
        null=False,
        blank=False
    )

    brand = ForeignKey(
        Brand,
        related_name='brand_model',
        on_delete=CASCADE
    )

    created = DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated = DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Car(Model):
    name = CharField(
        max_length=50,
        null=True,
        blank=True
    )

    description = CharField(
        max_length=200,
        null=True,
        blank=True
    )

    patent = CharField(
        max_length=200,
        null=True,
        unique=True,
        blank=True
    )

    size = CharField(
        max_length=200,
        null=False,
        blank=False
    )

    model = ForeignKey(
        CarModel,
        related_name='car_model',
        on_delete=CASCADE
    )

    number_of_doors = IntegerField(
        default=4,
        null=False,
        blank=False
    )

    diesel = BooleanField(
        default=False
    )

    created = DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated = DateTimeField(
        auto_now=True
    )

    image = ImageField(
        upload_to='core/static/products/cars/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Reservation(Model):

    client = ForeignKey(
        Profile,
        related_name='reservation_profile',
        on_delete=CASCADE
    )

    car = ForeignKey(
        Car,
        related_name='reservation_car',
        on_delete=CASCADE
    )

    start = DateTimeField(
        null=False,
        blank=False
    )

    end = DateTimeField(
        null=False,
        blank=False
    )

    created = DateTimeField(
        auto_now_add=True,
        editable=False
    )

    date_received = DateTimeField(
        null=True,
        blank=True
    )

    updated = DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.car.name} - {self.client.name}' 

    def save(self, *args, **kwargs):
        open_reservations = Reservation.objects.filter(
            client=self.client,
            date_received__isnull=True
        ).count()

        if open_reservations < 4:
            super(Reservation, self).save(*args, **kwargs)


