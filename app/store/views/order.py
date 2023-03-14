from django.urls import reverse
from django.views.generic import CreateView
from store.forms import OrderProductForm
from store.models import Order

from store.models import Cart


class OrderAddView(CreateView):
    template_name = 'order.html'
    model = Order
    form_class = OrderProductForm
    context_object_name = 'orders'

    def get_success_url(self):
        return reverse('cart_detail')
