from django.urls import path
from store.views.base import IndexView
from store.views.cart import CartAddView, CartDeleteView, CartDetailView
from store.views.category import CategoryView
from store.views.product import ProductAddView, ProductDetailView, ProductUpdateView, ProductDeleteView

from store.views.order import OrderAddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', IndexView.as_view(), name='products'),
    path('products/<str:category>', CategoryView.as_view(), name='categories'),
    path('product/add/', ProductAddView.as_view(), name='product_add'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),
]

urlpatterns += [
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('cart/order/', OrderAddView.as_view(), name='order_add'),
    path('cart/add/<int:pk>/', CartAddView.as_view(), name='cart_add'),
    path('cart/delete/<int:pk>/', CartDeleteView.as_view(), name='cart_delete'),
]
