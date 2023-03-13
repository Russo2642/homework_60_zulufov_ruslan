from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class CategoryChoice(TextChoices):
    PHONE = 'PHONE', 'Телефон'
    LAPTOP = 'LAPTOP', 'Ноутбук'
    CAMERA = 'CAMERA', 'Фотокамера'
    OTHER = 'OTHER', 'Другое'


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Наименование"
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=False,
        verbose_name="Описание"
    )
    image = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Фото"
    )
    category = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Категория",
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    rest = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Остаток"
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name="Стоимость"
    )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.category} - {self.title}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'title']
