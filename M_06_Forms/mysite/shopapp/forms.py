from django import forms
from .models import Product, Order
from django.forms import HiddenInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount", "archived"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "delivery_address", "promocode", "products", "user"
        widgets = {"user": HiddenInput()}
