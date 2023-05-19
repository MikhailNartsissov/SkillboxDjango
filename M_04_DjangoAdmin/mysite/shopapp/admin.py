from django.contrib import admin
from .models import Product
from django.db.models import TextField


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description_short", "price", "discount"
    list_display_links = "pk", "name"
    ordering = "price", "name"
    search_fields = "name", "description", "price"

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
