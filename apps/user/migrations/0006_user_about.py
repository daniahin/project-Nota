# Generated by Django 4.0.6 on 2022-09-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='О себе'),
        ),
    ]
