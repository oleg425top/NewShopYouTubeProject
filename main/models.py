from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.CharField(max_length=50, unique=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='Размер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
        ordering = ('id',)



class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_size', verbose_name='Товар')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    stock = models.PositiveIntegerField(default=0, verbose_name='Доступное кол-во')

    def __str__(self):
        return f'{self.size.name} ({self.stock} в наличии) для: {self.product.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.CharField(max_length=50, unique=True, verbose_name='Слаг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='products/main/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-created_at',)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(upload_to='product/extra/', verbose_name='Изображение')

