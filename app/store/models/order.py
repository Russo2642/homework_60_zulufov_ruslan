from django.db import models


class Order(models.Model):
    cart = models.ManyToManyField(
        'store.Product',
        related_name='order',
    )
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Телефон'
    )
    address = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Адрес'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def get_products(self):
        for product in self.cart.all():
            return product.title

    get_products.short_description = "Продукт"

    def get_total(self):
        total = 0
        for item in self.cart.all():
            total += item.get_total_price()
        return total

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.address}"
