from django.core.management.base import BaseCommand
from shopapp.models import Order
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    Class for new items creation in an orders table
    (i.e. for adding new orders into shop database)
    """
    def handle(self, *args, **options) -> None:
        """
        Command handler for the command "create_order"
        Creates new items in an orders table
        (i.e. adds new orders into shop database)
        :param args:
        :param options:
        :return: None
        """
        user_names = {
            "admin": ['ул. Ленина, д.1, кв.1', 'SALE2023'],
            "Pavel_X": ['ул. Штирлица, д. 17, кв. 17', 'ПЛЕЙШНЕР1945'],
            "Nartsissov@mail.ru": ['бульвар Монмартр, д.88а, кв.7', 'КИСА'],}
        for user_mame in user_names.keys():
            self.stdout.write("Trying to create an order...")
            user = User.objects.get(username=user_mame)
            order, created = Order.objects.get_or_create(
                delivery_address=user_names[user_mame][0],
                promo_code=user_names[user_mame][1],
                user=user,
            )
            if created:
                self.stdout.write((self.style.SUCCESS(f"Order {order.id} for user {user_mame} was created "
                                                      f"successfully")))
            else:
                self.stdout.write((self.style.ERROR(f"Order {order.id} already exists. Nothing to create.")))
        self.stdout.write(self.style.SUCCESS("Command executed successfully."))
