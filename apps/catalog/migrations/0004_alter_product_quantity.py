# Generated by Django 4.0.6 on 2022-08-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='Кількість'),
        ),
    ]