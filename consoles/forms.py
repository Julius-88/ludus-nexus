from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['console', 'tags', 'name', 'description', 'price', 'image']
        help_texts = {
            'tags': 'In order to select more than one tag, hold down "Ctrl" '
            'or "Cmd" on a Mac, and left click on each tag you want.'
        }
