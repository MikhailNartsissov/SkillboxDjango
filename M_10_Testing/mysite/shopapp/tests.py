from django.test import TestCase
from django.shortcuts import reverse
from django.conf import settings
from string import ascii_letters
from random import choices

from django.contrib.auth.models import User, Permission
from .models import Order, Product


class OrderDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob", password="qwerty")
        permission = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(permission)
        cls.product = Product.objects.create(
            name="".join(choices(ascii_letters, k=10))
        )
        cls.order = Order.objects.create(
            user=cls.user,
            delivery_address="".join(choices(ascii_letters, k=20)),
            promocode="".join(choices(ascii_letters, k=5))
        )
        cls.order.products.set([cls.product])

    @classmethod
    def tearDownClass(cls):
        cls.order.delete()
        cls.user.delete()
        cls.product.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_order_details_view(self):
        response = self.client.get(
            reverse("shopapp:order_details", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.promocode)
        self.assertContains(response, self.order.delivery_address)
        order = self.order.pk
        order_ = response.context['order'].pk
        self.assertEqual(order, order_)

    def test_order_details_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(
            reverse("shopapp:order_details", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class OrdersExportTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
        'orders-fixture.json',
        'users-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob", password="qwerty")
        permission = Permission.objects.get(codename="view_order")
        cls.user.user_permissions.add(permission)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_get_orders_view(self):
        response = self.client.get(
            reverse("shopapp:orders-export"),
        )
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "price": order.promocode,
                "user": order.user,
                "products": order.products,
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(
            orders_data["orders"],
            expected_data,
        )
