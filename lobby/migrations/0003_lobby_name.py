# Generated by Django 5.0.2 on 2024-02-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0002_lobby_participant_lobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='lobby',
            name='name',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]