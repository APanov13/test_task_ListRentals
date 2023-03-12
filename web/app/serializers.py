# Для тестирования отключена аутонтификация, что бы веруть необходимо -
# убрать комент с урлов и настройки(установленные приложения и внизу файла)

from rest_framework import serializers
from app.models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    """Сериализатор для взаимодействия с моделью Account"""
    transactions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('name', 'balance', 'transactions')
        read_only_fields = ('balance',)


class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для взаимодействия с моделью Transaction"""

    class Meta:
        model = Transaction
        fields = ('user_id', 'method', 'amound', 'timestamp')

    def create(self, validated_data):
        print(validated_data)
        if validated_data['method'] == 'WITHDRAW':
            if validated_data['user_id'].balance > validated_data['amound']:
                validated_data['user_id'].balance -= validated_data['amound']
                validated_data['user_id'].save()
            else:
                raise serializers.ValidationError(
                    ('Не достаточно средств на счете')
                )
            return super(TransactionSerializer, self).create(validated_data)
        elif validated_data['method'] == 'DEPOSIT':
            validated_data['user_id'].balance += validated_data['amound']
            validated_data['user_id'].save()
            return super(TransactionSerializer, self).create(validated_data)
