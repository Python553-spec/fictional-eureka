from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name','price']

        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Product Price', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Product Description', 'class': 'form-control'}),
        }
