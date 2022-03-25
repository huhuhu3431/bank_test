from rest_framework import serializers
from bank.models import Transaction

class TransactionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ("account", "value", "transaction_type", "comment")