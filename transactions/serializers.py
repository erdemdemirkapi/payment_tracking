from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'created_date', 'updated_date', 'note', 'user', 'amount_cents', 'amount_currency', 'state', 'to_whom', )
        depth = 1