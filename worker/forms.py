from django import forms
from authentication.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company_name', 'part_number', 'car_model', 'description', 'mrp', 'discount']
