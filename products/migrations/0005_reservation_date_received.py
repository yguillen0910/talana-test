# Generated by Django 3.0.7 on 2020-06-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200614_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_received',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
