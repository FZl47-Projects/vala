# Generated by Django 4.2.6 on 2023-12-28 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public', '0014_alter_post_image_alter_story_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Podcast text')),
                ('category', models.CharField(blank=True, max_length=128, null=True, verbose_name='دسته')),
                ('image', models.ImageField(upload_to='images/podcasts/', verbose_name='Podcast image')),
                ('audio', models.FileField(upload_to='audios/podcasts/', verbose_name='Podcast audio')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='podcasts', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcasts',
                'ordering': ('-id',),
            },
        ),
    ]
