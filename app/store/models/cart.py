from django.db import models


class Cart(models.Model):
    product = models.ForeignKey(
        'store.Product',
        related_name='basket',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quantity = models.IntegerField(
        null=True,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def total_price(self):
        return self.quantity * self.product.price

    def get_total_price(self):
        return self.total_price()

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"
