from rest_framework.response import Response
from rest_framework.views import APIView
from bank.models import Transaction
from bank.serializers import TransactionListSerializer


class TransactionListView(APIView):

    def get(self, request):
        transactions = Transaction.objects
        serializer = TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)