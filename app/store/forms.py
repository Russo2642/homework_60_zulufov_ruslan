from django import forms
from store.models import Product


class ProductForm(forms.ModelForm):
    rest = forms.IntegerField(min_value=1, error_messages={'min_value': 'Остаток не может быть меньше единицы.'})

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
