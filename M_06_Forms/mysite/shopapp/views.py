from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse

from .models import Product, Order
from .forms import ProductForm, OrderForm

from django.contrib import messages

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("shopapp:products_list")
            return redirect(url)
        elif form.errors['name']:
            messages.error(request, form.errors['name'])
    form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "shopapp/create-product.html", context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.username:
            form = OrderForm(request.POST)
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            url = reverse("shopapp:orders_list")
            return redirect(url)
        else:
            messages.error(request, "You must be authenticated to create orders")
            url = "/admin/"
            return redirect(url)
    form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, "shopapp/create-order.html", context=context)
