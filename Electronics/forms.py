from django import forms
from .models import Product

from django import forms
from .models import Product  # Adjust based on your model

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input block w-full p-2 rounded-md border border-gray-300'}),
            'price': forms.NumberInput(attrs={'class': 'form-input block w-full p-2 rounded-md border border-gray-300'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea block w-full p-2 rounded-md border border-gray-300', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-input block w-full p-2 rounded-md border border-gray-300'}),
        }