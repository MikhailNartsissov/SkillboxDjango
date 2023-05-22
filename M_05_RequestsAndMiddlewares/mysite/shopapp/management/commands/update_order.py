from django.core.management.base import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    """
    Class for adding new products into an existing orders
    (i.e. for updating existing orders in shop database with the products)
    """
    def handle(self, *args, **options) -> None:
        """
        Command handler for the command "update_order"
        Adds new products into an existing orders
        (i.e. updates existing orders in shop database with the products)
        :param args:
        :param options:
        :return: None
        """
        orders = Order.objects.all()
        if not orders:
            self.stdout.write(self.style.ERROR("No orders found"))
            return
        products = Product.objects.all()
        for order in orders:
            for product in products:
                order.products.add(product)
            order.save()
        self.stdout.write(self.style.SUCCESS("Command executed successfully."))
