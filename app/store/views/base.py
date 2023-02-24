from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View

from store.models import Product


class IndexView(View):
    def get(self, request: WSGIRequest):
        products = Product.objects.exclude(is_deleted=True)
        context = {
            'products': products
        }
        return render(request, 'index.html', context=context)
