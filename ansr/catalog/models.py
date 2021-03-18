from django.db import models
from django.shortcuts import reverse

from tinymce.models import HTMLField


class Product(models.Model):
    """ Продукт(Масло) """
    display = models.BooleanField(default=True, verbose_name='Отображается')
    carousel = models.BooleanField(default=False, verbose_name='Отображать в карусели')
    img = models.FileField(upload_to='images/', verbose_name='Изображение 1(Большое')
    img_mini = models.FileField(upload_to='images/', verbose_name='Изображение 1(миниатюра)')
    badge = models.CharField(max_length=15, null=True, blank=True, default=None, verbose_name='Бейдж')
    name = models.CharField(max_length=100, verbose_name='Название')

    health_description = HTMLField(verbose_name='Текст о здоровье', default='')
    health_image = models.ImageField(upload_to='product_description/', null=True, default=None)
    cooking_description = HTMLField(verbose_name='Текст о использовании в готовке', default='')
    cooking_image = models.ImageField(upload_to='product_description/', null=True, default=None,)
    cosmetology_description = HTMLField(verbose_name='Текст о косметологии', default='')
    cosmetology_image = models.ImageField(upload_to='product_description/', null=True, default=None,)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Ingredient(models.Model):
    """ Модель ингредиента продукта """
    types = (
        ('v', 'Витамины'),
        ('m', 'Минералы'),
        ('f', 'Жиры'),
        ('o', 'Остальное')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredients', verbose_name='Продукт')
    name = models.CharField(max_length=75, verbose_name='Название')
    type = models.CharField(max_length=20, choices=types, verbose_name='Тип')
    amount = models.CharField(max_length=50, verbose_name='На 100гр.')

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return 'Витамин: {}| Продукт: {}'.format(self.name, self.product.name)


class ProductAdvantage(models.Model):
    icon = models.FileField(upload_to='product_advantages/', null=True, blank=True, verbose_name='Иконка')
    title = models.CharField(max_length=30, verbose_name='Название преимущества')
    text = models.CharField(max_length=150, verbose_name='Описание преимущества')

    class Meta:
        verbose_name = 'преимущества покупки'
        verbose_name_plural = 'преимущества покупки'

    def __str__(self):
        return self.title


