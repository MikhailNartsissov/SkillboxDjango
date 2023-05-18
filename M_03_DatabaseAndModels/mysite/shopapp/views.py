from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer
from .models import Product


def shop_index(request: HttpRequest) -> HttpResponse:
    products = [
        ("Приворотное зелье", 1999,
         "https://i.pinimg.com/236x/32/72/39/3272398743d01e8b426dc469210cc177.jpg", True, None),
        ("Настойка от сглаза", 999,
         "https://i.pinimg.com/236x/a6/3d/57/a63d57a92465271c6f6fbf6899cc7b54.jpg", False, True),
        ("Эликсир мудрости", 2999,
         "https://i.pinimg.com/236x/b8/77/b3/b877b3872db9e844c2d9942a396e277c.jpg", None, False),
    ]
    properties = [
        'Эксклюзивный', 'Контрабандный', 'Уникальный',
    ]
    price_adv = [
        'Дешевле нет нигде во Вселенной!', 'Лучшей цены вам не найти!', 'Так дёшево бывает только в сказке!',
    ]
    context = {
        "products": products,
        "properties": properties,
        "price_adv": price_adv,
        "time_running": default_timer(),
    }
    return render(request, "shopapp/shop-index.html", context=context)


def products_list(request: HttpRequest) -> HttpResponse:
    context = {
        "products": Product.objects.all(),
    }
    return render(request, "shopapp/products-list.html", context=context)
