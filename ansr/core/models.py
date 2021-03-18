from django.db import models


class SiteSettings(models.Model):
    """ Настройки сайта """
    logo = models.FileField(upload_to='logo/', null=True, blank=True, verbose_name='Логотип')
    # Contacts
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='Электронная почта организации')
    site_email = models.CharField(max_length=50, null=True, blank=True, verbose_name='Электронная почта сайта',
                                  help_text='Почта для оповещений с сайта')
    font_page_header = models.FileField(upload_to='fonts/', null=True, blank=True,
                                        verbose_name='Шрифт заголовка страницы')
    font_block_header = models.FileField(upload_to='fonts/', null=True, blank=True,
                                         verbose_name='Шрифт заголовка блоков')
    font_product_header = models.FileField(upload_to='fonts/', null=True, blank=True,
                                           verbose_name='Шрифт заголовка товаров')
    font_additional = models.FileField(upload_to='fonts/', null=True, blank=True,
                                       verbose_name='Шрифт дополнительных текстов')

    # Colors
    buttons_color = models.CharField(max_length=20, null=True, blank=True, verbose_name='Цвет кнопок')

    class Meta:
        verbose_name = 'Общие настройки сайта'
        verbose_name_plural = 'Общие настройки сайта'

    def __str__(self):
        return 'Настройки'


