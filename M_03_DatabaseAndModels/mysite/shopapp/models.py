from django.db import models


class Product(models.Model):
    """
    Class for products description
    """
    name = models.CharField(null=False, blank=False, max_length=35, help_text="Наименование товара")
    description = models.TextField(null=False, blank=True, help_text="Описание товара")
    picture_url = models.URLField(default='https://cs6.pikabu.ru/avatars/547/v547695-2072060446.jpg', null=False)
    luck_in_business = models.BooleanField(default=False, null=False, help_text="Приносит ли товар удачу в бизнесе")
    curse_removes = models.BooleanField(default=False, null=False, help_text="Снимает ли товар порчу и сглаз")
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, help_text="Цена за единицу товара")
    discount = models.SmallIntegerField(default=0, help_text="Размер скидки в процентах")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время внесения товара в каталог")
