from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=256)
    # image = models.ImageField(verbose_name='Зображення', upload_to='blog/category', null=True)
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='blog/category',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія блога'
        verbose_name_plural = 'Категорії блога'

class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Article(models.Model):
    category = models.ForeignKey(
        to=BlogCategory,
        verbose_name='Категорія',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(to=Tag, verbose_name='Тэги', blank=True)
    image = ProcessedImageField(
        verbose_name='Зображеня',
        upload_to='blog/article',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True,
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
    )
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обнови', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
