from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'balance', 'is_superuser', 'created_date', 'iban', )