from django.contrib.admin import display
from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

from apps.catalog.models import Product
from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT


class Page(MetaTagMixin):
    name = models.CharField(verbose_name='Назва', max_length=128)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Опис', null=True)
    is_active = models.BooleanField(verbose_name='Активовано', default=True)


    class Meta:
        verbose_name = 'Інформаційна сторінка'
        verbose_name_plural = 'Інформаційні сторінки'

    def __str__(self):
        return self.name


class ProductSet(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=128)
    products = models.ManyToManyField(Product, verbose_name='Товари')
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(verbose_name='Активовано', default=True)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Карусель товарів'
        verbose_name_plural = 'Каруселі товарів'

    def __str__(self):
        return self.name


class GlobalSetting(MetaTagMixin):
    main_text = HTMLField(verbose_name='Текст на головній')
    footer_text = models.CharField(verbose_name='Текст у футері', max_length=255)
    logo = models.ImageField(verbose_name='Зображення', upload_to='main', null=True)

    @display(description='Текущий логотип')
    def image_tag_thumbnail(self):
        if self.logo:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.logo}' width='70'>")

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'

    def __str__(self):
        return 'Налаштування'

