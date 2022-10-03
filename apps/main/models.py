from django.db import models
from tinymce.models import HTMLField

from apps.main.mixins import MetaTagMixin


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
