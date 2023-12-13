# Generated by Django 4.2.6 on 2023-12-13 19:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=32, region=None, unique=True, verbose_name='شماره تماس')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='نشانی پست الکترونیکی')),
                ('first_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('access_level', models.CharField(choices=[('user', 'کاربر'), ('admin', 'Admin'), ('operator', 'Operator')], default='user', max_length=32, verbose_name='Access level')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
