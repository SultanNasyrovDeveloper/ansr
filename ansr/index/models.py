from django.db import models


class IndexPageSettings(models.Model):
    """ Настройки главной страницы """
    # SEO
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Title(seo tag)')
    keywords = models.CharField(max_length=150, null=True, blank=True, verbose_name='Keywords(seo tag)')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Description(Seo tag)')

    # banner caption
    h1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Заголовок баннера(h1)')
    banner_text = models.CharField(max_length=150, null=True, blank=True, verbose_name='Текст баннера')

    block_products_title = models.CharField(max_length=50, null=True, blank=True,
                                            verbose_name='Название блока карусель товаров')
    block_products_description = models.CharField(max_length=150, null=True, blank=True,
                                                  verbose_name='Описание блока карусель товаров')

    block_sale_background = models.FileField(upload_to='test/', verbose_name='Фон блока акция')
    block_sale_title = models.CharField(max_length=50, null=True, blank=True,
                                        verbose_name='Название блока акция')
    block_sale_subtitle = models.CharField(max_length=150, null=True, blank=True,
                                           verbose_name='Описание блока акция')
    block_sale_text = models.CharField(max_length=150, null=True, blank=True,
                                       verbose_name='Текст блока акция')
    block_aboutus_background = models.FileField(upload_to='about_us/', verbose_name='Задний фон блока о компании')
    block_aboutus_title = models.CharField(max_length=250, null=True, blank=True,
                                           verbose_name='Название блока о компании')
    block_aboutus_description = models.CharField(max_length=250, null=True, blank=True,
                                                 verbose_name='Описание блока о компании')
    block_aboutus_body = models.CharField(max_length=750, null=True, blank=True,
                                          verbose_name='Текст блока о компании')
    block_advantages_title = models.CharField(max_length=50, null=True, blank=True,
                                              verbose_name='Название блока приемущества')
    block_advantages_description = models.CharField(max_length=150, null=True, blank=True,
                                                    verbose_name='Описание блока приемущества')

    class Meta:
        verbose_name = 'настройки главной страницы'
        verbose_name_plural = 'настройки главной страницы'

    def __str__(self):
        return 'Настройки'


class IndexPageBanner(models.Model):
    """ Баннер главной страницы"""
    position = models.PositiveIntegerField(default=1, unique=True, verbose_name='Позиция')
    img = models.FileField(upload_to='banners/', verbose_name='Изображение')
    img_alt = models.CharField(max_length=150, verbose_name='Alt текст', help_text='Короткое описание изображения')

    class Meta:
        verbose_name = 'баннер'
        verbose_name_plural = 'баннеры'
        ordering = ('position', )

    def __str__(self):
        return 'Баннер №{}'.format(self.position)


class IndexPageAdvantages(models.Model):
    """  """
    icon = models.FileField(upload_to='advantages', verbose_name='Изображение')
    tagline = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.CharField(max_length=100, verbose_name='Текст')

    class Meta:
        verbose_name = 'преимущество'
        verbose_name_plural = 'преимущества'

    def __str__(self):
        return self.tagline


class IndexPageTestimonials(models.Model):
    """ Testimonials """
    name = models.CharField(max_length=100, verbose_name='Имя')
    organization = models.CharField(max_length=100, verbose_name='Организация')
    text = models.CharField(max_length=200, verbose_name='Текст отзыва')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return 'Отзыв от {}'.format(self.name)
