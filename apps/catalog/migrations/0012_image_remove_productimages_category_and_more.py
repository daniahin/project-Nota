# Generated by Django 4.0.6 on 2022-08-15 18:46

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_productimages_image_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/article', verbose_name='Зображеня')),
            ],
            options={
                'verbose_name': 'Категорія товару',
                'verbose_name_plural': 'Категорії товару',
            },
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='category',
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.image', verbose_name='Зображення'),
        ),
    ]
