# Generated by Django 4.2.1 on 2023-05-23 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_name_lala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name_lala',
        ),
    ]
