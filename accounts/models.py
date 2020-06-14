from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import OneToOneField
from django.db.models import CASCADE
from django.contrib.auth.models import User

class Profile(Model):
    GENDER = (
        ('f', 'Femenino'),
        ('m', 'Masculino')
    )

    name = CharField(
        max_length=200,
        null=False,
        blank=False
    )

    lastname = CharField(
        max_length=200,
        null=False,
        blank=False
    )

    gender = CharField(
        choices=GENDER,
        max_length=1,
        null=True,
        blank=True
    )

    rut = CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    user = OneToOneField(
        User,
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
