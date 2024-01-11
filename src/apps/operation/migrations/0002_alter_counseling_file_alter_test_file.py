# Generated by Django 4.2.6 on 2024-01-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counseling',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/counselings/2024-01-09/', verbose_name='فایل مشاوره'),
        ),
        migrations.AlterField(
            model_name='test',
            name='file',
            field=models.FileField(upload_to='files/tests/2024-01-09/', verbose_name='فایل آزمایش'),
        ),
    ]