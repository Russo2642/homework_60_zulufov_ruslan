from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DeleteView
from store.models import Cart
from store.models import Product


class CartDetailView(ListView):
    template_name = 'cart.html'
    model = Cart
    context_object_name = 'carts'


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart = Cart.objects.filter(product=product.pk)
        quantity = request.POST.get('quantity')
        if cart:
            for c in cart:
                if product.rest > c.quantity:
                    c.quantity += int(quantity)
                    c.save()
                else:
                    return redirect('index')
        else:
            if product not in cart and product.rest > 0:
                if product.rest >= int(quantity):
                    cart.create(
                        product=product,
                        quantity=int(quantity)
                    )

        return redirect('index')


class CartDeleteView(DeleteView):
    model = Cart

    def get_success_url(self):
        return reverse('cart_detail')
