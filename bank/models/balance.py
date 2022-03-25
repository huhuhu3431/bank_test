from django.db import models

# Create your models here.

class Balance(models.Model):

    account = models.CharField('Счёт клиента', max_length = 100)

    def __str__(self):
        return f'{self.account}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'