from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DeleteView
from store.forms import CartAddProductForm
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
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cart:
                for c in cart:
                    c.quantity += cd['quantity']
                    c.save()
            else:
                cart.create(
                    product=product,
                    quantity=cd['quantity']
                )
        return redirect('index')


class CartDeleteView(DeleteView):
    model = Cart

    def get_success_url(self):
        return reverse('cart_detail')
