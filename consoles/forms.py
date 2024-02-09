from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['console', 'tags', 'name', 'description', 'price', 'image']
