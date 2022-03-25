from bank.models import Balance
from bank.serializers import BalanceCreateSerializer
from rest_framework import viewsets,mixins


class BalanceOperationsView(viewsets.GenericViewSet,mixins.CreateModelMixin):

    queryset = Balance.objects.all()
    serializer_class = BalanceCreateSerializer