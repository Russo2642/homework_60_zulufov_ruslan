# Generated by Django 4.1.7 on 2023-02-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_created_at_product_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
