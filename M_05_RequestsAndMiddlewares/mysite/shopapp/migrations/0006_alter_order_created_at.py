# Generated by Django 4.2.1 on 2023-05-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата и время создания заказа'),
        ),
    ]
