from django.contrib import admin
from .models import Product, Order
from django.db.models import TextField, QuerySet
from django.http import HttpRequest


class ProductInline(admin.TabularInline):
    """
    Class for showing ordered products within the order
    """
    model = Order.products.through


class OrderInline(admin.TabularInline):
    """
    Class for showing orders, where the product is
    """
    model = Product.orders.through


@admin.action(description="Mark selected as Archived")
def mark_archived(model_admin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> None:
    """
    Marks selected records as archived
    :param model_admin:
    :param request:
    :param queryset:
    :return: None
    """
    queryset.update(archived=True)


@admin.action(description="Mark selected as Unarchived")
def mark_unarchived(model_admin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> None:
    """
    Marks selected records as unarchived
    :param model_admin:
    :param request:
    :param queryset:
    :return: None
    """
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Class for Product objects presentation in admin vew
    """
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = "price", "name"
    search_fields = "name", "description", "price"
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Ценовые параметры (цена за единицу, скидка и т.п.)", {
            "fields": ("price", "discount"),
            "classes": ("collapse", 'wide'),
        }),
        ("Дополнительные возможности (архивация и т.п.)", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Данный раздел является дополнительным. Атрибут 'Archived' можно использовать для "
                           "'мягкого удаления' записи (То есть, при необходимости, удалённую таким образом запись "
                           "можно легко восстановить)."
        }),
    ]

    @classmethod
    def description_short(cls, obj: Product) -> TextField:
        """
        Shortens presentation of the description in Products list
        :param obj: Product
        :return: TextField
        """
        if len(obj.description) <= 48:
            return obj.description
        return obj.description[:48] + "..."


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Class for Order objects presentation in admin vew
    """
    inlines = [
        ProductInline,
    ]
    list_display = "user_verbose", "delivery_address", "promo_code", "created_at"
    list_display_links = "user_verbose", "delivery_address", "created_at"
    ordering = "created_at", "user"
    search_fields = "user", "delivery_address", "created_at", "promo_code"

    def get_queryset(self, request: HttpRequest):
        """
        Optimizes user data queries for multiple users in database
        :param request:
        :return:
        """
        return Order.objects.select_related("user").prefetch_related("products")

    @classmethod
    def user_verbose(cls, obj: Order) -> str:
        """
        Shows user's first name if it is and username otherwise
        :return: str
        """
        return obj.user.first_name or obj.user.username
