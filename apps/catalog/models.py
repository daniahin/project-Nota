from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFill
from django.urls import reverse
from config.settings import MEDIA_ROOT


class Category(MPTTModel):
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Опис', blank=True, null=True)
    parent = TreeForeignKey(
        to='self',
        related_name='child',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='catalog/category',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
    )

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Поточне зображення'
    image_tag_thumbnail.allow_tags = True


    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Поточне зображення'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

class Product(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)
    description = models.TextField(verbose_name='Опис', blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    image = models.ManyToManyField(
        to='self',
        verbose_name='Зображення',
        through='ProductImages',
        related_name='images',
        blank=True
    )
    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категорії',
        through='ProductCategory',
        related_name='categories',
        blank=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, verbose_name='Категорія', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основна категорія', default=False)


    def __str__(self):
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductCategory.object.filter(product=self.product).update(is_main=False)
        super(ProductCategory, self).save(force_insert, force_update, using, update_fields)


    class Meta:
        verbose_name = 'Категорія товару'
        verbose_name_plural = 'Категорії товару'

class ProductImages(models.Model):
    image = ProcessedImageField(
        verbose_name='Зображеня',
        upload_to='blog/article',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
    )
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основне зображення', default=False)


    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Поточне зображення'
    image_tag_thumbnail.allow_tags = True


    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")


    def __str__(self):
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductImages.objects.filter(product=self.product).update(is_main=False)
        super(ProductImages, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Зображення товару'
        verbose_name_plural = 'Зображення товару'
