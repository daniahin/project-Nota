# Generated by Django 4.0.6 on 2022-08-11 14:26

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='user/', verbose_name='Зображеня'),
        ),
    ]
