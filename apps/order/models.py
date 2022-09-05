from django.db import models

from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)