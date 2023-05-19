# Generated by Django 4.2.1 on 2023-05-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_product_picture_url_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.TextField(blank=True, help_text='Адрес доставки заказа')),
                ('promo_code', models.CharField(blank=True, help_text='Промокод, примененный в заказе', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время внесения товара в каталог')),
            ],
        ),
    ]