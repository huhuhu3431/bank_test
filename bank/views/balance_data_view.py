from bank.models import Balance, Transaction
from bank.serializers import TransactionListSerializer, BalanceListSerializer
from rest_framework import viewsets,mixins
from django.db.models import Sum,Q,F
from django.db.models.functions import Coalesce


class BalanceDataView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Balance.objects.all()
    serializer_class = BalanceListSerializer

    def get_queryset(self):
        return self.queryset.annotate(
            deposit_sum=Coalesce(
                Sum(
                    'transactions__value', filter = Q(transactions__transaction_type='DP')
                ), 0
            ), withdrawal_sum = Coalesce(
                Sum(
                    'transactions__value', filter = Q(transactions__transaction_type='WD')
                ), 0
            )
        ).annotate(
        balance_qs=F('deposit_sum')-F('withdrawal_sum'))