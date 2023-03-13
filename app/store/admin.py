from django.contrib import admin
from store.models import Order
from store.models import Product
from store.models.cart import Cart


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'image',
        'category',
        'rest',
        'price',
        'is_deleted',
        'created_at',
        'updated_at',
        'deleted_at')
    list_filter = (
        'id',
        'title',
        'description',
        'image',
        'category',
        'rest',
        'price',
        'is_deleted',
        'created_at',
        'updated_at',
        'deleted_at')
    search_fields = ('id', 'title')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_products',
        'name',
        'phone',
        'address',
        'created_at'
    )
    list_filter = (
        'id',
        'name',
        'phone',
        'address',
        'created_at'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
