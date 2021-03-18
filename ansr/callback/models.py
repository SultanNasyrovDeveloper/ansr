from django.db import models


class Callback(models.Model):
    processed = models.BooleanField(default=False, verbose_name='Обработана', help_text='Да, если уже перезвонили')
    name = models.CharField(max_length=70, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'завяка на обратный звонок'
        verbose_name_plural = 'заявки на обратный звонок'

    def __str__(self):
        return 'Заявка от {}: {} - {}'.format(self.created.date(), self.name, self.phone)
