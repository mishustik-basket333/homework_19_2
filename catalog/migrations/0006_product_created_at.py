# Generated by Django 4.2.1 on 2023-05-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_product_category_remove_product_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата создания'),
        ),
    ]
