# Generated by Django 5.0.2 on 2024-02-07 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0003_lobby_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lobby',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(25), django.core.validators.MinValueValidator(0)]),
        ),
    ]
