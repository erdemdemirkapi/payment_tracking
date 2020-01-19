from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'user.username')
    to_whom_username = serializers.ReadOnlyField(source = 'to_whom.username')

    class Meta:
        model = Transaction
        fields = ('id', 'created_date', 'updated_date', 'note', 'user', 'username', 'amount_cents', 'amount_currency', 'state', 'to_whom', 'to_whom_username', )