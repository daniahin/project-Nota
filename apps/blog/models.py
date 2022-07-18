from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeFiel(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeFiel(verbose_name='Дата создания', auto_now=True)

