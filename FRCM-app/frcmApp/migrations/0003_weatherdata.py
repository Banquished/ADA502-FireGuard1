# Generated by Django 5.0.3 on 2024-04-23 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frcmApp', '0002_alter_weatherstation_options_weatherstation_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=6, max_digits=9)),
                ('humidity', models.DecimalField(decimal_places=6, max_digits=9)),
                ('wind_speed', models.DecimalField(decimal_places=6, max_digits=9)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather_data', to='frcmApp.weatherstation')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
