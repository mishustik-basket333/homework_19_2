from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Класс, для отображения категорий"""
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)  # Сортировка по имени


class Product(models.Model):
    """Класс, для отображения продуктов"""
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    create_data = models.DateField(auto_now_add=False, verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateField(auto_now_add=True, verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
        ordering = ('name',)  # Сортировка по имени
