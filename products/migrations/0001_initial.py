# Generated by Django 3.0.7 on 2020-06-14 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('patent', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('size', models.CharField(max_length=200)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_doors', models.IntegerField(default=4)),
                ('diesel', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_car', to='products.Car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_profile', to='accounts.Profile')),
            ],
        ),
    ]
