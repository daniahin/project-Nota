# Generated by Django 4.0.6 on 2022-08-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_options_alter_blogcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text_preview',
            field=models.TextField(null=True, verbose_name='Текст-превью'),
        ),
    ]
