from django.db import models
from django.db.models import TextChoices


# Create your models here.
class CategoryChoice(TextChoices):
    PHONE = 'PHONE', 'Телефон'
    LAPTOP = 'LAPTOP', 'Ноутбук'
    CAMERA = 'CAMERA', 'Фотокамера'
    OTHER = 'OTHER', 'Другое'


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name="Описание")
    image = models.CharField(max_length=200, null=False, blank=False, verbose_name="Фото")
    category = models.CharField(max_length=50, null=False, blank=False, verbose_name="Категория",
                                choices=CategoryChoice.choices, default=CategoryChoice.OTHER)
    rest = models.IntegerField(null=False, blank=False, verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return f"{self.category} - {self.title}"
