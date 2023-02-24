from django.contrib import admin
from store.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'category', 'rest', 'price')
    list_filter = ('id', 'title', 'description', 'image', 'category', 'rest', 'price')
    search_fields = ('id', 'title')


admin.site.register(Product, ProductAdmin)
