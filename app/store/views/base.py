from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View

from store.models import Product


class IndexView(View):
    def get(self, request: WSGIRequest):
        search_name = request.GET.get('search')
        if search_name:
            products = Product.objects.filter(is_deleted=False, title__icontains=search_name).exclude(rest=0)
        else:
            products = Product.objects.filter(is_deleted=False).exclude(rest=0)
        context = {
            'products': products
        }
        return render(request, 'index.html', context=context)
