# Generated by Django 4.2.6 on 2023-12-19 23:27

import apps.notification.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notificationuser_is_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationuser',
            name='number_id',
            field=models.CharField(default=apps.notification.models.random_number_id, max_length=10),
        ),
    ]
