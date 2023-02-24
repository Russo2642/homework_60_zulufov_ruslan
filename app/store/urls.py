from django.urls import path

from store.views.base import IndexView
from store.views.product import AddView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', IndexView.as_view(), name='products'),
    path('product/add/', AddView.as_view(), name='product_add'),
    path('product/<int:pk>', DetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', UpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', DeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', DeleteView.as_view(), name='confirm_delete'),
]
