from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from app.serializers import AccountSerializer, TransactionSerializer

from .models import Account, Transaction


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = PageNumberPagination


class TransactionVieSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination
