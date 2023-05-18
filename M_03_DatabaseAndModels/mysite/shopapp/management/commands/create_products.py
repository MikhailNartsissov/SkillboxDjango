from django.core.management.base import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """
    Class for new items creation in a shop's products table
    (i.e. for adding new products into shop database)
    """
    def handle(self, *args, **options) -> None:
        """
        Command handler for the command "create_products"
        Creates new items in a shop's products table
        (i.e. adds new products into shop database)
        :param args:
        :param options:
        :return: None
        """
        self.stdout.write("Trying to create products...")
        products_names = {
            "Приворотное зелье": ["https://i.pinimg.com/236x/32/72/39/3272398743d01e8b426dc469210cc177.jpg",
        1799, 0, 0, 10],
            "Настойка от сглаза": ["https://i.pinimg.com/236x/a6/3d/57/a63d57a92465271c6f6fbf6899cc7b54.jpg",
        1899, 0, 1, 5],
            "Эликсир мудрости": ["https://i.pinimg.com/236x/b8/77/b3/b877b3872db9e844c2d9942a396e277c.jpg",
        2999, 1, 0, 0],
        }
        for products_name in products_names.keys():
            product, created = Product.objects.get_or_create(name=products_name,
                                                             picture_url=products_names[products_name][0],
                                                             price=products_names[products_name][1],
                                                             luck_in_business=products_names[products_name][2],
                                                             curse_removes=products_names[products_name][3],
                                                             discount=products_names[products_name][4],
                                                             )
            if created:
                self.stdout.write((self.style.SUCCESS(f"Product {products_name} was created successfully")))
            else:
                self.stdout.write((self.style.ERROR(f"Product {products_name} already exists. Nothing to create.")))
        self.stdout.write(self.style.SUCCESS("Command executed successfully."))
