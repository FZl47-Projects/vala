# Generated by Django 4.2.6 on 2023-12-23 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartex', '0002_rename_laserbody_areabody'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areabody',
            old_name='description',
            new_name='note',
        ),
    ]
