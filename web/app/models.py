from django.db import models

CHOICES = (
        ('DEPOSIT', 'deposit'),
        ('WITHDRAW', 'withdraw'),
    )


class Account(models.Model):
    """Модель пользователя и его баланса"""
    name = models.CharField(max_length=20)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=9)

    def __str__(self):
        return f'Аккаунт ID: {self.id}, владелец :{self.name}'


class Transaction(models.Model):
    """Модель всех типов транзакций"""
    user_id = models.ForeignKey(
        Account, related_name='transactions', on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=CHOICES)
    amound = models.DecimalField(decimal_places=2, max_digits=9)
    timestamp = models.DateTimeField(
        'дата и время',
        auto_now_add=True,
    )

    def __str__(self):
        return f'№ {self.id}, {self.timestamp}, {self.method}, {self.amound}'
