# Generated by Django 5.0.3 on 2024-03-28 17:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frcmApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherstation',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
