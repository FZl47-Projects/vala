# Generated by Django 4.2.6 on 2024-01-06 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_access_options_alter_access_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.CharField(choices=[('basic', 'Basic'), ('vip', 'VIP')], default='basic', max_length=32, verbose_name='Profile level'),
        ),
        migrations.AlterField(
            model_name='access',
            name='title',
            field=models.CharField(choices=[('user', 'کاربر'), ('admin', 'ادمین'), ('op', 'اپراتور'), ('diet_op', 'اپراتور تغذیه'), ('workout_op', 'اپراتور ورزشی')], max_length=64, unique=True, verbose_name='عنوان دسترسی'),
        ),
    ]
