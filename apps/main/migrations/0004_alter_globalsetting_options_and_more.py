# Generated by Django 4.0.6 on 2022-10-13 14:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_globalsetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalsetting',
            options={'verbose_name': 'Налаштування', 'verbose_name_plural': 'Налаштування'},
        ),
        migrations.AlterField(
            model_name='globalsetting',
            name='footer_text',
            field=models.CharField(max_length=255, verbose_name='Текст у футері'),
        ),
        migrations.AlterField(
            model_name='globalsetting',
            name='logo',
            field=models.ImageField(null=True, upload_to='main', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='globalsetting',
            name='main_text',
            field=tinymce.models.HTMLField(verbose_name='Текст на головній'),
        ),
    ]