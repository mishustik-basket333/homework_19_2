import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        category_data = []
        product_data = []
        with open('data.json', encoding='utf-8') as f:
            data = json.load(f)

        for raw in data:
            if raw["model"] == "catalog.category":
                category_data.append(Category(**raw["fields"]))
            if raw["model"] == "catalog.product":
                product_data.append(Product(**raw["fields"]))

        Category.objects.all().delete()
        Product.objects.all().delete()

        Category.objects.bulk_create(category_data)
        Product.objects.bulk_create(product_data)

        print("Были удалены все данные из таблиц: Category, Product\n"
              "Добавлены новые данные из файла 'data.json' в эти таблицы")
