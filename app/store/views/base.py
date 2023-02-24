from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View

from store.models import Product


class IndexView(View):
    def get(self, request: WSGIRequest):
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request, 'index.html', context=context)
