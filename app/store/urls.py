from django.urls import path

from app.store.views.base import IndexView
from app.store.views.product import AddView, DetailView, UpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', AddView.as_view(), name='product_add'),
    path('product/<int:pk>', DetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', UpdateView.as_view(), name='product_update'),
    # path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
    # path('todo/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
]