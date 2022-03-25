from bank.models import Transaction
from bank.serializers import TransactionListSerializer
from rest_framework import viewsets,mixins


class TransactionOperationsView(viewsets.GenericViewSet,mixins.CreateModelMixin):

    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer