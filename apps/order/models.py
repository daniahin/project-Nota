from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=0)
    first_name = models.CharField(verbose_name="Ім'я", max_length=32)
    last_name = models.CharField(verbose_name="Прізвище", max_length=32)
    email = models.EmailField(verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Телефон', null=True, blank=True)
    address = models.TextField(verbose_name='Адреса')
    comment = models.TextField(verbose_name='Коментар', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обнови', auto_now=True)


    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='Товар', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Кількість')
    price = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=0, default=0)

    class Meta:
        verbose_name = 'Товар з замовлення'
        verbose_name_plural = 'Товари з замовлення'
