from django.db.models import Q
from django.shortcuts import render
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, TemplateView
from store.forms import SearchForm
from store.models import Product

from store.forms import CartAddProductForm

from store.models import CategoryChoice


# class IndexView(ListView):
#     template_name = 'index.html'
#     model = Product
#     form = CartAddProductForm()
#     context_object_name = 'products'
#     ordering = ('-created_at',)
#     paginate_by = 5
#     paginate_orphans = 1




    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    #
    # def get_search_form(self):
    #     return SearchForm(self.request.GET)
    #
    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(is_deleted=False).exclude(rest=0)
    #     if self.search_value:
    #         query = Q(title__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #     return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context


class IndexView(View):
    def get(self, request):
        search_name = request.GET.get('search')
        cart_product_form = CartAddProductForm()
        if search_name:
            products = Product.objects.filter(is_deleted=False, title__icontains=search_name).exclude(rest=0)
        else:
            products = Product.objects.filter(is_deleted=False).exclude(rest=0)
        context = {
            'products': products,
            'choices': CategoryChoice.choices,
            'cart_product_form': cart_product_form
        }
        return render(request, 'index.html', context=context)