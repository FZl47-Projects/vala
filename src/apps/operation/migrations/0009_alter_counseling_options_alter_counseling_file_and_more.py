# Generated by Django 4.2.6 on 2024-01-04 21:09

import apps.operation.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0008_alter_counseling_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='counseling',
            options={'ordering': ('-id',), 'verbose_name': 'مشاوره', 'verbose_name_plural': 'مشاوره\u200cها'},
        ),
        migrations.AlterField(
            model_name='counseling',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/counselings/2024-01-04/', verbose_name='فایل مشاوره'),
        ),
        migrations.AlterField(
            model_name='counseling',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='counseling',
            name='is_answered',
            field=models.BooleanField(default=False, verbose_name='پاسخ داده'),
        ),
        migrations.CreateModel(
            name='SkinRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('image1', models.ImageField(blank=True, null=True, upload_to=apps.operation.utils.upload_routine_image, verbose_name='Full face image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to=apps.operation.utils.upload_routine_image, verbose_name='Right face image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to=apps.operation.utils.upload_routine_image, verbose_name='Left face image')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skin_routines', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'Skin routine',
                'verbose_name_plural': 'Skin routines',
                'ordering': ('-id',),
            },
        ),
    ]
