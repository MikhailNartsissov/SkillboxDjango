from csv import DictReader
from io import TextIOWrapper

from django.contrib.auth.models import User

from shopapp.models import Order


def save_csv_orders(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding,
    )
    reader = DictReader(csv_file)
    for row in reader:
        order = Order()
        order.delivery_address = row["delivery_address"]
        order.promocode = row["promocode"]
        order.receipt = row["receipt"]
        order.user = User.objects.get(pk=row["user"])
        order.save()
        order.products.add(row["products"])
