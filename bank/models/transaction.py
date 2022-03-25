from django.db import models
from django.utils.translation import gettext_lazy as _
from .balance import Balance

# Create your models here.

class Transaction(models.Model):

    class TransactionType(models.TextChoices):
        DEPOSIT = "DP", _("Deposit")
        WITHDRAW = "WD", _("Withdraw")

    account = models.ForeignKey(Balance, on_delete=models.CASCADE, related_name="transactions")
    value = models.PositiveIntegerField('Значение')
    transaction_type = models.CharField('Тип операции (зачисление/вывод)', choices = TransactionType.choices, max_length=10)
    comment = models.CharField('Комментарий', max_length=100)

    def __str__(self):
        return f'{self.account}, {self.transaction_type} {self.value} рублей с комментарием: {self.comment}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'