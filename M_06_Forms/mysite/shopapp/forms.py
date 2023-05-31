from django import forms
from .models import Product, Order
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount", "archived"

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].isalpha():
            return name
        raise ValidationError("Product name must start with literal")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "delivery_address", "promocode", "products"
