from django import forms
from store.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'rest', 'price')
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'image': 'Ссылка на картинку',
            'category': 'Категория',
            'rest': 'Остаток',
            'price': 'Цена'
        }
