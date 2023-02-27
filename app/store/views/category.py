from django.shortcuts import render
from django.views import View
from store.models import Product, CategoryChoice


class CategoryView(View):
    def get(self, request, category):
        search_name = request.GET.get('search')
        if search_name:
            products = Product.objects.filter(is_deleted=False, category=category,
                                              title__icontains=search_name).exclude(rest=0).order_by('title')
        else:
            products = Product.objects.filter(is_deleted=False, category=category).exclude(rest=0).order_by('title')
        return render(request, 'category.html', context={
            'products': products,
            'choices': CategoryChoice.choices
        })
