# Generated by Django 4.0.6 on 2022-08-15 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_images_alter_productimages_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.images', verbose_name='Зображення'),
        ),
    ]
