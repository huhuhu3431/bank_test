from rest_framework import serializers
from bank.models import Balance

class BalanceListSerializer(serializers.ModelSerializer):

    balance = serializers.CharField(source="balance_qs")

    class Meta:
        model = Balance
        fields = ("account","balance")