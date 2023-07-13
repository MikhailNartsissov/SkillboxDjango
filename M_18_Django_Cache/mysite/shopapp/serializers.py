from rest_framework import serializers

from .models import Product, Order
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "discount",
            "created_at",
            "archived",
            "preview",
        )


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "price",
        )


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserOrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True)
    user = OrderUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['user', 'pk', 'created_at', 'delivery_address', 'products', 'promocode']
