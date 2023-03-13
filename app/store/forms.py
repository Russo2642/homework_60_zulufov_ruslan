from django import forms
from store.models import Order
from store.models import Product


class ProductForm(forms.ModelForm):
    rest = forms.IntegerField(label='Остаток', min_value=1,
                              error_messages={'min_value': 'Остаток не может быть меньше единицы.'})

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'category', 'rest', 'price']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'image': 'Ссылка на картинку',
            'category': 'Категория',
            'rest': 'Остаток',
            'price': 'Цена'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class CartAddProductForm(forms.Form):
    quantity = forms.DecimalField(label='Количество', min_value=1)


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'address': 'Адрес'
        }
