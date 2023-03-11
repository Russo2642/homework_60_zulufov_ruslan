from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from store.forms import ProductForm
from store.models import Product


class ProductAddView(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product


class ProductUpdateView(UpdateView):
    template_name = 'update_product.html'
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
