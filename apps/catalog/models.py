from django.contrib.admin import display
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFill
from django.urls import reverse

from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT


class Category(MPTTModel, MetaTagMixin):
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


class Image(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='catalog/product',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100}
    )
    product = models.ForeignKey(to='Product', verbose_name='Товар', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основне Зображення', default=False)

    @display(description='Поточне зображення')
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    @display(description='Поточне зображення')
    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                Image.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    def __str__(self):
        return ''


class Product(MetaTagMixin):
    name = models.CharField(verbose_name='Назва', max_length=255)
    description = models.TextField(verbose_name='Опис', blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=0, default=0)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)
    categories = models.ManyToManyField(
        to=Category,
        verbose_name='Категорії',
        through='ProductCategory',
        related_name='categories',
        blank=True
    )

    def images(self):
        return Image.objects.filter(product=self.id)

    def main_image(self):
        image = Image.objects.filter(is_main=True, product=self.id).first()
        if image:
            return image
        return self.images().first()

    def main_category(self):
        category = self.categories.filter(productcategory__is_main=True).first()
        if category:
            return category
        return self.categories.first()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.id})


class ProductCategory(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, verbose_name='Категорія', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основна категорія', default=False)


    def __str__(self):
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_main:
            ProductCategory.objects.filter(product=self.product).update(is_main=False)
        super(ProductCategory, self).save(force_insert, force_update, using, update_fields)


    class Meta:
        verbose_name = 'Категорія товару'
        verbose_name_plural = 'Категорії товару'
