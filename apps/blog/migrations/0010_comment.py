# Generated by Django 4.0.6 on 2022-10-07 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_alter_article_text_alter_article_text_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255, verbose_name='Нікнейм')),
                ('email', models.CharField(max_length=255, verbose_name='Е-меіл')),
                ('text', tinymce.models.HTMLField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обнови')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]
