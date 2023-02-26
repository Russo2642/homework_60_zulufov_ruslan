from django.contrib import admin
from store.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'image', 'category', 'rest', 'price', 'is_deleted', 'created_at', 'updated_at',
        'deleted_at')
    list_filter = (
        'id', 'title', 'description', 'image', 'category', 'rest', 'price', 'is_deleted', 'created_at', 'updated_at',
        'deleted_at')
    search_fields = ('id', 'title')


admin.site.register(Product, ProductAdmin)
