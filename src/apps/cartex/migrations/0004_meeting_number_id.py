# Generated by Django 4.2.6 on 2023-12-23 23:06

import apps.cartex.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartex', '0003_rename_description_areabody_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='number_id',
            field=models.CharField(default=apps.cartex.models.random_number_id, max_length=10),
        ),
    ]
